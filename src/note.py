from functools import total_ordering

from duration import Note_Type, Time_Modification
from pitch import Pitch, Rest
from pitch import Diatonic_Pitch as Unpitched

STEM_DIRECTION = { # "double" not implemented.
    "up": 2,
    "down": 0,
    "none": 1,
}

class Chord_Common_Data(Note_Type): # The common data among chord notes.
    def __init__(self):
        super(Chord_Common_Data, self).__init__()
        self._stem = STEM_DIRECTION["none"]
        self._time_modification = None
    def __eq__(self, other):
        try:
            return super(Chord_Common_Data, self).__eq__(other) \
                and self._stem == other._stem \
                and self._time_modification == other._time_modification
        except TypeError: # Two instances have time_modification of different types.
            return False
    def __ne__(self, other):
        return not (self == other)
    @property
    def stem(self):
        return self._stem
    @stem.setter
    def stem(self, value):
        self._stem = STEM_DIRECTION[value]
    @property
    def time_modification(self):
        return self._time_modification
    @time_modification.setter
    def time_modification(self, value):
        if self._time_modification is None:
            self._time_modification = Time_Modification()
        self._time_modification.actual_notes = value[0]
        self._time_modification.normal_notes = value[1]
        self._time_modification.normal_type = value[2]
        self._time_modification.normal_dot = value[3]

@total_ordering
class Chord_Individual_Data(object): # The individual data for each chord note.
    def __init__(self):
        self._duration = 0
        self._pitch = None
        self._staff = 1
    def __eq__(self, other):
        return hash(self) == hash(other)
    def __hash__(self):
        return hash((type(self), self._pitch))
    def __lt__(self, other):
        return self._pitch < other._pitch
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        value = int(value)
        assert value > 0
        self._duration = value
    @property
    def pitch_type(self): # [!] No setter.
        return type(self._pitch)
    @property
    def pitch(self):
        assert type(self._pitch) is Pitch
        return self._pitch
    @pitch.setter
    def pitch(self, value):
        self._pitch = Pitch()
        (self._pitch.step, self._pitch.alter, self._pitch.octave) = value
    @property
    def rest(self):
        assert type(self._pitch) is Rest
        return self._pitch
    @rest.setter
    def rest(self, value):
        self._pitch = Rest()
        (self._pitch.display_step, self._pitch.display_octave) = value
    @property
    def staff(self):
        return self._staff
    @staff.setter
    def staff(self, value):
        value = int(value)
        assert value > 0
        self._staff = value
    @property
    def unpitched(self):
        assert type(self._pitch) is Unpitched
        return self._pitch
    @unpitched.setter
    def unpitched(self, value):
        self._pitch = Unpitched()
        (self._pitch.display_step, self._pitch.display_octave) = value

class Note(Chord_Common_Data):
    def __init__(self):
        super(Note, self).__init__()
        self._chord = tuple()
        self._duration_ref = 0
        self._staff_ref = 0
    def __hash__(self):
        return hash((type(self), self._chord))
    def __lt__(self, other):
        if self.staff != other.staff: return self.staff > other.staff
        if type(self._chord[0]._pitch) is Pitch and type(other._chord[0]._pitch) is Pitch:
            if self._stem != other._stem: return self._stem < other._stem
        return self._chord[0]._pitch.__lt__(other._chord[0]._pitch)
    @property
    def chord(self): # [!] No setter.
        return self._chord
    def chord_append(self, new_data):
        self._chord += (new_data,)
        if new_data.duration > self._chord[self._duration_ref].duration:
            self._duration_ref = len(self._chord) - 1 # Don't use negative index.
    def chord_sort(self):
        self._chord = tuple(sorted(self._chord))
        self._duration_ref = self._chord.index(max(self._chord, key=lambda p: p.duration))
    @property
    def duration(self):
        return self._chord[self._duration_ref].duration if self._chord else 0
    @property
    def staff(self): # [!] No setter.
        return self._chord[self._staff_ref].staff if self._chord else 1
    @property
    def stem(self):
        return super(Note, self).stem
    @stem.setter
    def stem(self, value):
        type(self).__base__.stem.fset(self, value)
        self._staff_ref = -1 if super(Note, self).stem == STEM_DIRECTION["down"] else 0
