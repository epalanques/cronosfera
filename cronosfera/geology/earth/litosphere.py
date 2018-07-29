import subprocess as sp
from cronosfera.geology.earth.rocks.rock import RockManager

class Litosphere:
    def __init__(self):
        self.continents = ''
        self.ocean = ''
        self.rock_registry = []  # Llista de <roques> del periode
        self._rock_manager = RockManager()

    def get_info(self):
        # todo: D'on agafa el nom el txt?
        info_path = 'cronosfera/geology/concepts/%s.txt' % self.info_file
        sp.Popen(["open", info_path])

    def add_register(self):
        # todo: el registry poden ser roques o formacions senceres. Què rep com a parametre?
        pass




"""
* Escorça fosa o sòlida
* Oceans existeixen o no
* Roques del periòde (amb classificació)




"""