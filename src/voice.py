import weakref

from note import *
from pitch import *
from py2to3compatibility import *
from score import *

def organize(current_block, staves):
    voice_change = put_weakref(current_block, staves)
    for t in voice_change:
        for i in xrange(len(voice_change[t])):
            voice_change[t][i]

def put_weakref(current_block, staves):
    continued_notes = (set(), set())
    voice_count = dict((i, [0, 0]) for i in xrange(1, staves + 1))
    voice_change = {}
    for t in sorted(dict_iterkeys(current_block)):
        for n_t in continued_notes[0]: # Remove stopped notes.
            if n_t[1] + n_t[0].duration <= t: # It is the end of the note.
                continued_notes[1].add(n_t)
        continued_notes[0].difference_update(continued_notes[1])
        for n in current_block[t]: # Notes starting from now.
            n.chord_sort()
            continued_notes[1].add((n, t))
        for n_t in continued_notes[0]: # Add weakrefs to continuing notes.
            current_block[t].append(weakref.ref(n_t[0]))
        for l in dict_itervalues(voice_count):
            l[0], l[1] = l[1], 0 # [0]: The previous; [1]: The current.
        for n in current_block[t]: # All notes including weakrefs.
            voice_count[n().staff][1] += 1
        for k in dict_iterkeys(voice_count):
            if voice_count[k][0] != voice_count[k][1]:
                try:
                    voice_change[t].append([k])
                except KeyError:
                    voice_change[t] = [[k]]
                voice_change[t][-1] += voice_count[k]
                if [x for x in continued_notes[0] if x[0].staff == k]: # Number of voices changes with continuing notes.
                    pass
        current_block[t].sort(key=lambda x: x())
        continued_notes[0].update(continued_notes[1])
        continued_notes[1].clear()
    return voice_change
