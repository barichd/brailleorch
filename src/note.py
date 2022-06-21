# Copyright (C) 2016-2022 BrailleOrch

from __future__ import unicode_literals
from collections import OrderedDict
from collections import namedtuple
from enum import Enum
from fractions import Fraction
import math

class Pitch(namedtuple("Pitch", ["octave", "step", "alter"])):
    _Step_Offset = namedtuple("_Step_Offset", ["diatonic", "midi"])
    _step2offset = dict(zip("CDEFGAB", (
        _Step_Offset(diatonic=0, midi=0),  # C
        _Step_Offset(diatonic=1, midi=2),  # D
        _Step_Offset(diatonic=2, midi=4),  # E
        _Step_Offset(diatonic=3, midi=5),  # F
        _Step_Offset(diatonic=4, midi=7),  # G
        _Step_Offset(diatonic=5, midi=9),  # A
        _Step_Offset(diatonic=6, midi=11), # B
    )))
    def __new__(cls, octave, step, alter=None):
        octave = int(octave)
        if octave < 0 or octave > 9: raise ValueError(octave)
        step = str(step)
        if step not in cls._step2offset: raise ValueError(step)
        if alter is not None: # None indicates the displayed pitch.
            alter = float(alter)
            if math.isinf(alter) or math.isnan(alter): raise ValueError(alter)
        return super(Pitch, cls).__new__(cls, octave, step, alter)
    def __lt__(self, other):
        return (self.octave, self.step, self.alter) < (other.octave, other.step, other.alter)
    def __str__(self): # The absolute pitch.
        if self.octave > 3:
            return "{0}{1}".format(self.step.lower(), self.octave - 3)
        elif self.octave == 3:
            return self.step.lower()
        elif self.octave == 2:
            return self.step.upper()
        return "{0}{1}".format(self.step.upper(), 2 - self.octave)
    def __sub__(self, other):
        diatonic_pitch = lambda obj: len(obj._step2offset) * obj.octave + obj._step2offset[obj.step].diatonic
        return diatonic_pitch(self) - diatonic_pitch(other)
    @property
    def alter(self):
        return .0 if self.unpitched else super(type(self), self).alter
    @property
    def unpitched(self):
        return super(type(self), self).alter is None
    def midi(self, round_microtone=False):
        if self.alter is None: raise TypeError
        from math import copysign
        midi_step = self._step2offset[self.step].midi
        answer = 12 * (self.octave + 1) + midi_step
        if round_microtone:
            answer += int(copysign(round(abs(self.alter)), self.alter))
        elif not self.alter.is_integer(): raise ValueError("Invalid midi value: {0}".format(answer + self.alter))
        else:
            answer += int(self.alter)
        if answer < 12 or answer > 127: raise ValueError("Invalid midi value: {0}".format(answer))
        return answer

class Type(object):
    values = (
        "maxima",
        "long",
        "breve",
        "whole",
        "half",
        "quarter",
        "eighth",
        "16th",
        "32nd",
        "64th",
        "128th",
        "256th",
        "512th",
        "1024th",
    )
    def __init__(self, value, dots=0):
        self._index, self._delta = 0, 0
        self.value, self.dots = value, dots
    def __repr__(self):
        return "{0}('{1}', dots={2})".format(self.__class__.__name__, self.value, self.dots)
    def __str__(self):
        t = self.value
        return ("{1}-dot {0} note" if self._delta > 0 else "{0} note").format(t, self.dots)
    @property
    def dots(self):
        return self._delta
    @dots.setter
    def dots(self, value):
        if value < 0: raise ValueError(value)
        elif value == 0:
            if self._delta > 0:
                self._index += 1
        elif self._delta < 1 :
            self._index -= 1
        self._delta = value
    @property
    def time(self):
        t = Fraction(1, 2) ** self._index
        if self._delta > 0:
            t -= Fraction(1, 2) ** (self._index + self._delta + 1)
        return t * 8
    @property
    def value(self):
        return self.values[self._index + int(self._delta > 0)]
    @value.setter
    def value(self, new_value):
        self._index = self.values.index(new_value)
        self._delta = 0

class Time_Modification(object):
    def __init__(self, normal_type=None):
        self._ratio = [1, 1]
        self.normal_type = normal_type
    @property
    def actual_notes(self):
        return self._ratio[1]
    @actual_notes.setter
    def actual_notes(self, n):
        if n <= 0: raise ValueError(n)
        self._ratio[1] = n
    @property
    def normal_notes(self):
        return self._ratio[0]
    @normal_notes.setter
    def normal_notes(self, n):
        if n <= 0: raise ValueError(n)
        self._ratio[0] = n
    @property
    def ratio(self):
        return Fraction(*self._ratio)
    @property
    def tuplet_time(self):
        return self.normal_notes * self.normal_type.time

class Stem(Enum):
    DOWN = "down"
    NONE = "none"
    UP = "up"
    DOUBLE = "double"
    def __lt__(self, other):
        if self == Stem.DOWN: return other != Stem.DOWN
        elif self in (Stem.NONE, Stem.DOUBLE): return other == Stem.UP
        return False
    def __str__(self):
        return "no stem" if self == Stem.NONE else "stem {0}".format(self.value)

class Beam_Type(Enum):
    BEGIN = "begin"
    CONTINUE = "continue"
    END = "end"
    FORWARD_HOOK = "forward hook"
    BACKWARD_HOOK = "backward hook"

def _add_int_id(attr_name, init_value):
    def wrapper(cls):
        def getter(self):
            return getattr(self, "_" + attr_name)
        def setter(self, value):
            if not isinstance(value, int) or value <= 0: raise ValueError(value)
            setattr(self, "_" + attr_name, value)
        setattr(cls, "_" + attr_name, init_value)
        setattr(cls, attr_name, property(getter, setter))
        return cls
    return wrapper

@_add_int_id("voice", 1)
class _Basic_Note(object):
    @_add_int_id("staff", 1)
    class Head(object):
        def __init__(self):
            self.pitch = Pitch(4, "C")
        def __lt__(self, other):
            if self.staff > other.staff:
                return True
            elif self.staff < other.staff:
                return False
            return self.pitch < other.pitch
        def __str__(self):
            return "{0} at staaff {1}".format(self.pitch, self.staff)
        @property
        def pitch(self):
            return self._pitch
        @pitch.setter
        def pitch(self, value):
            self._pitch = value if isinstance(value, Pitch) else Pitch(*value)
    def __init__(self):
        self._type = Type("whole")
        self._time_modification = Time_Modification()
        self._stem = Stem("none")
        self.beam = None
    @property
    def beam(self):
        return self._beam
    @beam.setter
    def beam(self, value):
        if value is not None and not isinstance(value, Beam_Type):
            value = Beam_Type(value)
        self._beam = value
    @property
    def chord(self):
        raise NotImplementedError
    @property
    def display(self):
        raise NotImplementedError
    @property
    def duration(self):
        return 0
    @property
    def staff(self):
        raise NotImplementedError
    @property
    def time(self):
        return self.type.time * Fraction(self.time_modification.normal_notes, self.time_modification.actual_notes)
    @property
    def time_modification(self):
        return self._time_modification
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        if not isinstance(value, Type):
            value = Type(value)
        self._type = value
    @property
    def stem(self):
        return self._stem
    @stem.setter
    def stem(self, value):
        if not isinstance(value, Stem):
            value = Stem(value)
        self._stem = value

class Grace_Note(_Basic_Note): # TODO: Support of make-time.
    class Head(_Basic_Note.Head):
        def __init__(self):
            super(type(self), self).__init__()
            self.pitch = Pitch(4, "C", .0)
    slash = False
    steal_time_previous = .0
    steal_time_following = .0
    def __init__(self):
        super(type(self), self).__init__()
        self._chord = []
    @property
    def chord(self):
        return self._chord
    def auto(self):
        return self.steal_time_previous, self.steal_time_following == .0, .0

class Regular_Note(_Basic_Note):
    class Head(_Basic_Note.Head):
        def __init__(self):
            super(type(self), self).__init__()
            self.pitch = Pitch(4, "C", .0)
            self.duration = 1
        @property
        def duration(self):
            return self._duration
        @duration.setter
        def duration(self, value):
            if not isinstance(value, int) or value <= 0: raise ValueError(value)
            self._duration = value
    def __init__(self):
        super(type(self), self).__init__()
        self._chord = []
    @property
    def chord(self):
        return self._chord
    @property
    def display(self):
        if not self.chord: raise TypeError("no display position for an empty note")
        h = self.chord[len(self.chord) >> 1]
        return type(h.pitch)(h.pitch.octave, h.pitch.step)
    @property
    def duration(self):
        if len(self.chord) > 0:
            return max(n.duration for n in self.chord)
        return 0
    @duration.setter
    def duration(self, value):
        if not self.chord:
            raise TypeError("empty note")
        for c in self.chord:
            c.duration = value
    @property
    def staff(self):
        if not self.chord: raise TypeError("no display position for an empty note")
        return self.chord[len(self.chord) >> 1].staff

@_add_int_id("staff", 1)
class Rest(_Basic_Note):
    @classmethod
    def pad(cls, time, reference):
        if (time.denominator & (time.denominator - 1)) != 0: # Not a power of 2.
            raise ValueError("can't pad time {0}".format(time))
        answer, b = [], Type.values.index("whole") + time.denominator.bit_length() - 1
        for i in range(min(time.numerator.bit_length(), b)):
            if time.numerator & (1 << i):
                answer.append(cls())
                answer[-1].display = reference[0].display
                answer[-1].type = Type.values[b - i]
                answer[-1].staff = reference[0].staff
        for i in range(time.numerator >> b):
            answer.append(cls())
            answer[-1].display = reference[0].display
            answer[-1].type = Type.values[0]
            answer[-1].staff = reference[0].staff
        return answer
    chord = None
    def __init__(self):
        super(type(self), self).__init__()
        self.measure_time = Fraction(0)
        self.display = None
        self.duration = 1
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        if not isinstance(value, int) or value <= 0: raise ValueError(value)
        self._duration = value
    @property
    def display(self):
        return self._pitch
    @display.setter
    def display(self, value):
        if value is not None:
            if not isinstance(value, Pitch):
                value = Pitch(value)
            if not value.unpitched: raise ValueError(value)
        self._pitch = value
    @property
    def pitch(self): # Convenient for names.
        return self.display
    @property
    def time(self):
        return self.measure_time if self.measure_time > 0 else super(type(self), self).time
