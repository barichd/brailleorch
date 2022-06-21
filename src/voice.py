# Copyright (C) 2016-2022 BrailleOrch

from __future__ import unicode_literals
from note import *
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import weakref
class Note(object):
    def __init__(self, note, divisions):
        self.notes = [note]
        if not isinstance(note, Rest):
            note.chord.sort(reverse=True)
        self.divisions = divisions
    def __lt__(self, other):
        if self.staff_range < other.staff_range:
            return False
        elif self.staff_range > other.staff_range:
            return True
        if not isinstance(self.notes[0], Rest) and not isinstance(other.notes[0], Rest):
            if self.notes[0].stem < other.notes[0].stem:
                if self.notes[0].stem == "none":
                    if other.notes[0].lowest_notehead.pitch < self.notes[0].lowest_notehead.pitch:
                        return False
                elif other.notes[0].stem == "none":
                    if other.notes[0].highest_notehead.pitch < self.notes[0].highest_notehead.pitch:
                        return False
                return True
            elif other.notes[0].stem < self.notes[0].stem:
                if other.notes[0].stem == "none":
                    if self.notes[0].lowest_notehead.pitch < other.notes[0].lowest_notehead.pitch:
                        return True
                elif self.notes[0].stem == "none":
                    if self.notes[0].highest_notehead.pitch < other.notes[0].highest_notehead.pitch:
                        return True
                return False
        if self.highest_notehead.pitch is not None and other.highest_notehead.pitch is not None:
            if other.highest_notehead.pitch < self.highest_notehead.pitch:
                return False
            elif self.highest_notehead.pitch < other.highest_notehead.pitch:
                return True
        if self.lowest_notehead.pitch is not None and other.lowest_notehead.pitch is not None:
            if other.lowest_notehead.pitch < self.lowest_notehead.pitch:
                return False
            elif self.lowest_notehead.pitch < other.lowest_notehead.pitch:
                return True
        return self.notes[0].voice > other.notes[0].voice
    @property
    def highest_notehead(self):
        return self.notes[0] if isinstance(self.notes[0], Rest) else self.notes[0].chord[0]
    @property
    def lowest_notehead(self):
        return self.notes[0] if isinstance(self.notes[0], Rest) else self.notes[0].chord[-1]
    @property
    def staff_range(self):
        return (self.lowest_notehead.staff, self.highest_notehead.staff)

    def combine(self, other):
        if isinstance(self.notes[0], Rest) or isinstance(other.notes[0], Rest): raise TypeError
        if self.divisions != other.divisions: raise TypeError
        p, s = (other, self) if self.notes[0].time > other.notes[0].time else (self, other)
        if not set((n.pitch, n.staff) for n in s.notes[0].chord).issubset(set((n.pitch, n.staff) for n in p.notes[0].chord)):
            raise TypeError("Notes of different pitches.")
        if self is p:
            self.notes += other.notes
        else:
            self.notes = other.notes + self.notes
        self.notes.sort(key=lambda n: n.time)
    def distance(self, other):
        h, l = (self.highest_notehead, other.highest_notehead), (self.lowest_notehead, other.lowest_notehead)
        d = [abs(h[0].staff - h[1].staff), 0]
        if h[0].pitch is not None and h[1].pitch is not None:
            d[1] = abs(h[0].pitch - h[1].pitch)
        if h[0] is not h[1] or l[0] is not l[1]:
            d[0] += abs(l[0].staff - l[1].staff)
            if l[0].pitch is not None and l[1].pitch is not None:
                d[1] += abs(l[0].pitch - l[1].pitch)
        return tuple(d)

class Voice(defaultdict):
    def __init__(self):
        super(Voice, self).__init__(list)
    def __call__(self, time, precise=True):
        try:
            if precise:
                t = min((t for t in self if t <= time), key=lambda t: time - t)
            else:
                t = min((t for t in self if t < time), key=lambda t: time - t)
        except: raise IndexError(time)
        answer = self[t] # To call __getitem__.
        if len(answer) < 1 and t < time: raise IndexError(time)
        return answer
    def __getitem__(self, index):
        class _const_list:
            def __init__(self, note_list):
                self._list = note_list
            def __bool__(self):
                return bool(self._list)
            def __iter__(self):
                return iter(self._list)
            def __len__(self):
                return len(self._list)
            def __repr__(self):
                return repr(self._list)
            def __str__(self):
                return str(self._list)
            def __getitem__(self, i):
                return self._list[i]
            def append(_self, note):
                _self._list.append(note)
                self[index + note.notes[0].time]
            def extend(_self, other):
                for n in other:
                    _self._list.append(n)
            def reverse(self, *args, **kwargs):
                return self._list.reverse(*args, **kwargs)
            def sort(self, *args, **kwargs):
                return self._list.sort(*args, **kwargs)
        return _const_list(super(type(self), self).__getitem__(index))
    def analyze(self, pos):
        all_voices, current_voices = [], []
        for t, m in sorted(self.items(), key=lambda t: t[0]):
            m.sort(reverse=True)
            l, d = [], [] # l: Indices of ready voices in current_voices.
            if current_voices:
                for i in range(len(current_voices)):
                    try:
                        if len(current_voices[i]()(t)) < 1: # Ready for the next note.
                            l.append(i)
                    except IndexError: # The voice is discontinued.
                        d.append(i)
            else: # The first loop.
                l = list(range(len(m)))
                for i in l:
                    all_voices.append(Voice())
                    current_voices.append(weakref.ref(all_voices[-1]))
            for i in reversed(d):
                del current_voices[i]
                l = list(l[j] - int(l[j] > i) for j in range(len(l)))
            if len(l) != len(m): # Find the optimal mapping from current_voices to the next notes.
                weight = {}
                s = [list(range(len(l))), list(range(len(m)))]
                for x in product(*s):
                    n_l, pr = current_voices[l[x[0]]]()(t, False)[0], 1
                    if n_l.notes[0].voice == m[x[1]].notes[0].voice: # Special cases indicated by <voice>.
                        if n_l.notes[0].beam in (Beam_Type.BEGIN, Beam_Type.CONTINUE):
                            if isinstance(m[x[1]].notes[0], Rest):
                                m[x[1]].notes[0].beam = Beam_Type.CONTINUE
                            if m[x[1]].notes[0].beam in (Beam_Type.CONTINUE, Beam_Type.END):
                                pr = 0
                    weight[x] = (pr,) + n_l.distance(m[x[1]])
                while weight: # A greedy algorithm to pick the lightest first.
                    x = min(weight.items(), key=lambda x: x[1])[0]
                    s[0].remove(x[0])
                    s[1].remove(x[1])
                    for y in list(weight.keys()):
                        if y[0] == x[0] or y[1] == x[1]:
                            del weight[y]
                for j in reversed(s[0]):
                    del current_voices[l[j]]
                    del l[j]
                    for k in range(j, len(l)):
                        l[k] -= 1
                if s[1]:
                    for j in s[1]:
                        all_voices.append(Voice())
                        if j < len(l):
                            current_voices.insert(l[j], weakref.ref(all_voices[-1]))
                            l.insert(j, l[j])
                        else:
                            l.append(len(current_voices))
                            current_voices.append(weakref.ref(all_voices[-1]))
                        for k in range(j + 1, len(l)):
                            l[k] += 1
            for v, n in zip((current_voices[j] for j in l), m):
                v()[t].append(n)
        pending_voice_ids, melodies = [], []
        for i in range(len(all_voices)):
            if (min(all_voices[i]), max(all_voices[i])) == (min(self), max(self)):
                melodies.append((i, weakref.ref(all_voices[i])))
            else:
                pending_voice_ids.append(i)
        for x in combinations(melodies, 2):
            try:
                x[0][1]().zip(x[1][1]())
                all_voices[x[1][0]] = None
            except:
                pass
        melodies = list(v for v in all_voices if v is not None and (min(v), max(v)) == (min(self), max(self)))
        for i, u in zip(pending_voice_ids, (all_voices[j] for j in pending_voice_ids)):
            for v in sorted((m for m in melodies if min(u) in m), key=lambda m: m[min(u)][0].distance(u[min(u)][0])):
                try:
                    v.zip(u)
                    break # The case of successfull zip.
                except: # Try to combine them together.
                    try:
                        Voice().update(v).update(u).in_accord_map()
                        v.update(u)
                        break
                    except:
                        pass
            else: # No voice can be combined with voice u.
                for v in sorted(melodies, key=lambda m: m(min(u))[0].distance(u[min(u)][0])):
                    slot, time_range = None, [None, min(v)]
                    for s in v.in_accord_map():
                        time_range[0], time_range[1] = time_range[1], time_range[1] + sum(n.notes[0].time for n in s[0])
                        if time_range[0] <= min(u) and max(u) <= time_range[1]:
                            slot = s
                            break # Success.
                    if slot is not None:
                        pad = [Rest.pad(min(u) - time_range[0], u[min(u)][0].notes), Rest.pad(time_range[1] - max(u), u(max(u), precise=False)[0].notes)]
                        for r in reversed(pad[0]):
                            r.duration = int(4 * u[min(u)][0].divisions * r.time)
                            v[time_range[0]].append(Note(r, u[min(u)][0].divisions))
                            time_range[0] += r.time
                        v.update(u)
                        time_range[1] = max(u)
                        for r in pad[1]:
                            r.duration = int(4 * u[min(u)][0].divisions * r.time)
                            v[time_range[1]].append(Note(r, u[min(u)][0].divisions))
                            time_range[1] += r.time
                        print("!t", v.in_accord_map())
                        break # Success.
                else:
                    raise TypeError("{0}: can't handle voices".format(pos))
            all_voices[i] = None
        pending_voice_ids = list(i for i in pending_voice_ids if all_voices[i] is not None)
        if pending_voice_ids:
            raise RuntimeError("algorithm failed")
        return melodies
    def in_accord_map(self):
        answer, current_state = [], []
        for t in sorted(self):
            l = list(i for i in range(len(current_state)) if current_state[i] == t)
            if len(l) != len(self[t]):
                if not all(s == t for s in current_state):
                    raise TypeError("Failure occurs at {0} when parsing music data [{1}, {2}]".format(t, min(self), max(self)))
                answer.append(list([] for v in self[t]))
                current_state = [t] * len(self[t])
                l = range(len(current_state))
            for p in zip(l, self[t]):
                answer[-1][p[0]].append(p[1])
                current_state[p[0]] += p[1].notes[0].time
        if not answer[-1]: # This should be the normal case.
            del answer[-1]
        if answer and not all(len(t) > 0 for t in answer):
            raise TypeError("Failure occurs at {0} when parsing music data [{1}, {2}]".format(t, min(self), max(self)))
        return answer
    def update(self, other):
        if not isinstance(other, type(self)): raise TypeError
        for t in other:
            self[t].extend(other[t])
        return self
    def zip(self, other):
        result = type(self)()
        for t in sorted(set(self) | set(other)):
            if t in other:
                result[t].extend(other[t])
                if t in self and self[t]:
                    result[t][0].combine(self[t][0])
            else:
                result[t].extend(self[t])
        self.update(result)
        return self
