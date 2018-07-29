import subprocess as sp

from cronosfera.events import Event


class GeologicEvent(Event):
    #todo: Un Manager: tindrem Earth que tindrá: composició (litosfera i atmòsfera) i formació
    #todo: Un petit rock manager intern que permetrá identificar la família de roques
    def __init__(self, tipus, name, year, end_year=None):
        super().__init__(name, year, end_year)
        self.tipus = tipus

    def get_geologic_info(self):
        info_path = 'cronosfera/geology/concepts/%s.txt' % self.tipus
        sp.Popen(["open", info_path])
