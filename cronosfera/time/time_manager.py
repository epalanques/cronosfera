from cronosfera.time import Time, TIME_ORDER
from cronosfera.events import Event
from cronosfera.geology.geologic_event import GeologicEvent


class TimeManager(Time):

    def __init__(self):
        super().__init__("Manager", "Earth existence", 4600000000, 0)
        self.subperiods_type = 'supereons'

    def add(self, tipus, name, starting_year, end_year=None):
        # Lowercase the type
        tipus = tipus.lower()

        # Time period
        if tipus in TIME_ORDER:
            period = Time(tipus, name, starting_year, end_year)
            self.add_period(period)
        # Event
        elif tipus == 'event':
            event = Event(name, starting_year, end_year)
            if end_year:
                self.add_duration_event(event)
            else:
                self.add_punctual_event(event)
        # Geological event
        else:
            geo_event = GeologicEvent(tipus, name, starting_year)
            if end_year:
                self.add_duration_event(geo_event)
            else:
                self.add_punctual_event(geo_event)
