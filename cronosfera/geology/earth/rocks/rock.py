import subprocess as sp
import h5py

class Rock:

    # todo: Rework: passar a sql

    def __init__(self, name):
        self.name = name
        self.type = [] # llista amb els seus sobretipus
        self.composition = []
        self.subclassifications = {}
        self.other_names = []
        self.info_path = 'cronosfera/geology/concepts/rocks/%s.txt' % self.name
        # Nomes per quan l'usuari vol realment utilizar un altre path


    def add_mineral(self, elements):
        for element in elements:
            self.composition.append(element)

    def get_info(self):
        return sp.Popen(["open", self.info_path])

    def add_subclass(self, name):  # Has test
        assert type(name) == str
        assert name not in self.subclassifications.keys(), "Subclass %s already exists" % name

        self.subclassifications[name] = Rock(name)

        return self.subclassifications[name]

    def _create_full_path(self, path):  # Has test
        path = path.split("/")
        superficial_layer = path[0]

        superficial_layer_rock = self.get_subclass(superficial_layer)
        if not superficial_layer_rock:
            superficial_layer_rock = self.add_subclass(superficial_layer)

        if len(path) > 1:
            superficial_layer_rock._create_full_path("/".join(path[1:]))

    def add_other_names(self, names):  # Has test
        assert type(names) == list, "Names have to be imputed as a list"
        for name in names:
            assert type(name) == str, "Name has to ba a string"
            self.other_names.append(name)

    def _get_rock(self, rock):  # Has test
        rock_found = self.get_subclass(rock)

        if rock_found:
            return rock_found
        else:
            if self.is_final():
                return
            else:
                for subclass in self.subclassifications.values():
                    return subclass._get_rock(rock)

    def get_subclass(self, subclass):  # Has test
        subclass = [rock for rock in self.subclassifications.values()
                    if (rock.name == subclass or subclass in rock.other_names)]
        assert len(subclass) <= 1
        if subclass:
            return subclass[0]
        else:
            return

    def __contains__(self, item):  # Has test
        return self.get_subclass(item) is not None

    def is_final(self):
        return not self.subclassifications


class RockManager(Rock):
    def __init__(self):
        super().__init__("Manager")

    def create_full_path(self, path):  # Has Test
        super()._create_full_path(path)

    def get_rock(self, rock):  # Has Test
        return super()._get_rock(rock)


    # todo: get rock examples
    # Si li entres un tipus de roca (ex: ultramafica) et retorna una llista amb les roques
    # ultramafiques que te guardades.
    # Totes o un maxim de unes 5 per no acumular?

def rock_classification():
    rock_manager = RockManager()
    rock_manager.create_full_path("")
