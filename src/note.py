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
        self._staff = 1
        self._stem = STEM_DIRECTION["none"]
        self._time_modification = None
    @property
    def staff(self):
        return self._staff
    @staff.setter
    def staff(self, value):
        value = int(value)
        assert value > 0
        self._staff = value
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

class Chord_Individual_Data(object): # The individual data for each chord note.
    def __init__(self):
        self._duration = 0
        self._pitch = None
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        value = int(value)
        assert value > 0
        self._duration = value
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
    def unpitched(self):
        assert type(self.chord[0]._pitch) is Unpitched
        return self._pitch
    @unpitched.setter
    def unpitched(self, value):
        self._pitch = Unpitched()
        (self._pitch.display_step, self._pitch.display_octave) = value

class Note(Chord_Common_Data):
    def __init__(self):
        super(Note, self).__init__()
        self._chord = []
    def __lt__(self, another):
        if self._staff > another.staff: return True
        elif self._staff < another.staff: return False
        if type(self._chord[0]._pitch) is Pitch and type(another._chord[0]._pitch) is Pitch:
            if self._stem < another._stem: return True
            elif self._stem > another._stem: return False
        return self._chord[0]._pitch.__lt__(another._chord[0]._pitch)
    @property
    def chord(self): # [!] No setter.
        return self._chord
