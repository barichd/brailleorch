from __future__ import print_function
# from lxml import etree
import xml.etree.cElementTree as etree
import sys

from note import *
from pitch import *
from score import *

class XMLAnalyzer:
    handlers = {
        "backup": "parse_backup",
        "forward": "parse_forward",
        "measure": "parse_measure",
        "note": "parse_note",
        "part": "parse_part",
        "part-list": "loop_over_children",
        "part-name": "parse_part_name",
        "score-part": "parse_score_part",
    }
    parse = lambda self, node: getattr(self, self.handlers[node.tag])(node)
    def __init__(self, path):
        root = etree.parse(path).getroot()
        self.score = Score()
        if root.tag == "score-partwise":
            self.parse_part = self.read_part
            self.parse_measure = self.read_music_data
        else:
            self.parse_part = self.read_music_data
            self.parse_measure = self.read_measure
        self.loop_over_children(root)
    def loop_over_children(self, parent):
        for child in parent:
            try:
                self.parse(child)
            except KeyError:
                pass
    def read_music_data(self, music_data_parent):
        self.loop_over_children(music_data_parent)
    def read_part(self, part_node): # Partwise score only.
        current_part_id = part_node.get("id")
        self.t, self.t_max = 0, 0
        for measure in part_node.iterfind("measure"):
            self.current_block = self.score(current_part_id, measure.get("number"), True)
            self.current_note = None
            self.previous_note = None
            self.t = max(self.t, self.t_max)
            self.read_music_data(measure)
        del self.current_block
        del self.current_note
        del self.previous_note
    def parse_backup(self, node):
        self.t_max = max(self.t_max, self.t)
        self.t -= int(node.find("duration").text)
    def parse_forward(self, node):
        self.t += int(node.find("duration").text)
    def parse_note(self, xml_note):
        self.current_note = Note()
        chord_data = Chord_Individual_Data()
        is_chord = False
        for node in xml_note:
            if node.tag == "duration":
                chord_data.duration = node.text
            elif node.tag == "type":
                self.current_note.type = node.text
            elif node.tag == "dot":
                self.current_note.dot += 1
            elif node.tag == "stem":
                self.current_note.stem = node.text
            elif node.tag == "staff":
                self.current_note.staff = node.text
            elif node.tag in {"pitch", "rest", "unpitched"}:
                if node.tag=="pitch":
                    chord_data.pitch = (node.findtext("step"), node.findtext("alter", "0"), node.findtext("octave"))
                elif node.tag=="rest":
                    chord_data.rest = (node.findtext("display-step"), node.findtext("display-octave"))
                    chord_data.rest.measure = node.get("measure", "no")
                else:
                    chord_data.unpitched = (node.findtext("display-step"), node.findtext("display-octave"))
            elif node.tag == "time-modification":
                value = [node.findtext("actual-notes"), node.findtext("normal-notes"),
                         node.findtext("normal-type"), len(node.findall("normal-dot"))]
                if value[2] is None:
                    value[2] = self.current_note.type
                if value[3] == 0:
                    value[3] = self.current_note.dot
            elif node.tag == "chord":
                is_chord = True
            elif node.tag in ("grace", "cue"):
                return
        if is_chord:
            if chord_data.pitch_type is Rest: # A rest note is in the chord.
                self.current_note.chord.append(chord_data)
                self.current_block.append(self.current_note)
            elif Chord_Common_Data.__eq__(self.current_note, self.previous_note):
                self.previous_note.chord.append(chord_data)
            else: # The common data changes within a chord.
                self.current_note.chord.append(chord_data)
                self.current_block.append(self.current_note)
                self.previous_note = self.current_note
        else:
            self.t += chord_data.duration
            self.current_note.chord.append(chord_data)
            self.current_block.append(self.current_note)
            self.previous_note = self.current_note
    def parse_part_name(self, xml_part_header):
        self.current_part_header.name = xml_part_header.text
    def parse_score_part(self, node):
        self.current_part_header = self.score.add_part(node.get("id"))
        self.loop_over_children(node)
        del self.current_part_header

s = XMLAnalyzer(sys.argv[1]).score
print(len(s.part_list), len(s.measures))
