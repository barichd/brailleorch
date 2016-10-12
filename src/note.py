from pitch import Pitch, Rest
from pitch import Diatonic_Pitch as Unpitched

class Note(object):
    def __init__(self):
        self._duration = 0
        self._pitch = None
    def __lt__(self, another):
        return self._pitch.__lt__(another._pitch)
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
        setattr(self, "_pitch", Pitch())
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
        assert type(self._pitch) is Unpitched
        return self._pitch
    @unpitched.setter
    def unpitched(self, value):
        self._pitch = Unpitched()
        (self._pitch.display_step, self._pitch.display_octave) = value
