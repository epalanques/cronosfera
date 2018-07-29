

class Mineral:

    def __init__(self, name):
        self.name = name
        self.composition = []

    def add_composition(self, element):
        self.composition.append(element)

