class Music_Data_Block(dict):
    def __init__(self):
        self._begin_time = 0
    def add(self, t, data):
        t -= self.begin_time
        try:
            self[t].append(data)
        except KeyError:
            self[t] = [data]
    @property
    def begin_time(self):
        return self._begin_time
    @begin_time.setter
    def begin_time(self, value):
        value = int(value)
        assert value >= 0
        self._begin_time = value

class Measure:
    def __init__(self, score, number):
        self.number = number
        self.score = score
        self.data = [Music_Data_Block() for k in range(len(self.score.part_list))]

class Part(object):
    def __init__(self, id):
        self.id = id
        self.name = ""
        self._staves = 1
    @property
    def staves(self):
        return self._staves
    @staves.setter
    def staves(self, value):
        value = int(value)
        assert value > 0
        self._staves = value

class Score:
    def __init__(self):
        self.part_id_map = {}
        self.part_list = []
        self.measure_number_map = {}
        self.measures = []
    def __call__(self, id, number, no_create=True):
        try: # Add a new part if needed.
            id = self.part_id_map[id]
        except KeyError as e:
            if id is not None:
                if no_create:
                    raise e
                self.part_id_map[id] = len(self.part_list)
                self.part_list.append(Part(id))
                for m in self.measures:
                    m.append([]) # An element mapped to the new part.
                id = -1
        if number is None: # This fails when id is also None.
            return self.part_list[id]
        try: # Add a new measure if needed.
            number = self.measure_number_map[number]
        except KeyError as e:
            if no_create:
                raise e
            self.measure_number_map[number] = len(self.measures)
            self.measures.append(Measure(self, number))
            number = -1
        if id is None:
            return self.measures[number]
        return self.measures[number].data[id]
    def iter_part(self, id):
        for m in measures:
            yield m[id]
