from cronosfera.events import Event
import subprocess as sp


class GeologicEvent(Event):
    #todo: Un Manager: tindrem Earth que tindrá dos components: composició (litosfera i atmòsfera) i formació
    #todo: Un petit rock manager intern que permetrá identificar la família de roques
    def __init__(self, type, name, year, end_year=None):
        super().__init__(name, year, end_year)
        self.type = type

    def get_geologic_info(self):
        info_path = 'cronosfera/geology/concepts/%s.txt' % self.type
        sp.Popen(["open", info_path])
