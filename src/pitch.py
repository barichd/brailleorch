class Diatonic_Pitch(object): # General displayed pitch (<unpitched> included).
    def __init__(self):
        self._alter = .0
        self._octave = 4
        self._step = self._step2midi['C']
    def __lt__(self, another):
        if self._octave < another._octave: return True
        elif self._octave > another._octave: return False
        if self._step < another._step: return True
        elif self._step > another._step: return False
        return self._alter < another._alter
    @property
    def alter(self):
        raise NotImplementedError("This is only implemented by Pitch.")
    @alter.setter
    def alter(self, value):
        raise NotImplementedError("This is only implemented by Pitch.")
    @property
    def display_octave(self):
        return self._octave
    @display_octave.setter
    def display_octave(self, value):
        if value is not None:
            value = int(value)
            assert 0 <= value and value <= 9
        self._octave = value
    _step2midi = dict(zip(('C', 'D', 'E', 'F', 'G', 'A', 'B'), (0, 2, 4, 5, 7, 9, 11)))
    @property
    def display_step(self):
        return self._step
    @display_step.setter
    def display_step(self, value):
        self._step = value if value is None else self._step2midi[value]

class Pitch(Diatonic_Pitch): # Regular-note pitch.
    def __init__(self):
        super(Pitch, self).__init__()
    @property
    def alter(self):
        return self._alter
    @alter.setter
    def alter(self, value):
        value = float(value)
        self._alter = value
    def midi(self):
        return self.step + round(self.alter) + 12 * (self.octave + 1)
    @property
    def octave(self):
        return self.display_octave
    @octave.setter
    def octave(self, value):
        self.display_octave = value
    @property
    def step(self):
        return self.display_step
    @step.setter
    def step(self, value):
        assert value is not None
        self.display_step = value

class Rest(Diatonic_Pitch): # Rest-note pitch.
    def __init__(self):
        super(Rest, self).__init__()
        self._measure = False
    @property
    def measure(self):
        return self._measure
    @measure.setter
    def measure(self, value):
        if type(value) is str:
            assert value in ("yes", "no")
        else:
            assert type(value) is bool
        self._measure = value
