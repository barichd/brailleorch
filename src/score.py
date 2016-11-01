class Measure:
    def __init__(self, score, number):
        self.number = number
        self.score = score
        self.data = [[] for k in range(len(self.score.part_list))]

class Part:
    def __init__(self, id):
        self.id = id
        self.name = ""

class Score:
    def __call__(self, id, number, create_if_not_exist=False):
        id = self.part_id_map[id]
        try:
            number = self.measure_number_map[number]
            return self.measures[number].data[id]
        except KeyError as e:
            if not create_if_not_exist:
                raise e
            self.measure_number_map[number] = len(self.measures)
            self.measures.append(Measure(self, number))
            return self.measures[-1].data[id]
    def __init__(self):
        self.part_id_map = {}
        self.part_list = []
        self.measure_number_map = {}
        self.measures = []
    def add_part(self, id):
        if id in self.part_id_map:
            raise Exception("Multiple part ID:" + id)
        self.part_id_map[id] = len(self.part_list)
        self.part_list.append(Part(id))
        for m in self.measures:
            m.append([])
        return self.part_list[-1]
    def iter_part(self, id):
        for m in measures:
            yield m[id]
