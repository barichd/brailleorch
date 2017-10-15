NOTE_TYPE = (
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

class Note_Type(object):
    def __init__(self):
        self._dot = 0
        self._type = "whole"
    def __eq__(self, other):
        return self.type == other.type and self.dot == other.dot
    def __ne__(self, other):
        return not (self == other)
    def __repr__(self):
        return "<%s type=%s dot=%d>" % (str(self.__class__)[1:-1], self.type, self.dot)
    @property
    def dot(self):
        return self._dot
    @dot.setter
    def dot(self, value):
        assert value >= 0
        self._dot = value
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        if type(value) is int:
            assert 0 <= value and value < len(NOTE_TYPE)
        else:
            value = NOTE_TYPE.index(value)
            assert value >= 0
        self._type = value

class Time_Modification(object):
    def __init__(self):
        self._normal = Note_Type()
        self._notes = [1, 1]
    def __eq__(self, other):
        return self._normal == other._normal and self._notes == other._notes
    def __ne__(self, other):
        return not (self == other)
    @property
    def actual_notes(self):
        return self._notes[1]
    @actual_notes.setter
    def actual_notes(self, value):
        value = int(value)
        assert value > 0
        self._notes[1] = value
    @property
    def normal_notes(self):
        return self._notes[0]
    @normal_notes.setter
    def normal_notes(self, value):
        value = int(value)
        assert value > 0
        self._notes[0] = value
    @property
    def normal_dot(self):
        return self._normal.dot
    @normal_dot.setter
    def normal_dot(self, value):
        self._normal.dot = value
    @property
    def normal_type(self):
        return self._normal.type
    @normal_type.setter
    def normal_type(self, value):
        self._normal.type = value
