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
    def __eq__(self, another):
        return self.type == another.type and self.dot == another.dot
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
