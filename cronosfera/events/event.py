from cronosfera.events import EventBase


class Event(EventBase):

    def __init__(self, name, starting_year, end_year=None):
        super().__init__(name, starting_year)

        self.starting_year = starting_year
        self.starting_event = self._create_starting_event()

        if end_year:
            self.end_year = end_year
            self.ending_event = self._create_ending_event()

    def _create_starting_event(self):
        return EventBase(self.name+"_start", self.starting_year)

    def _create_ending_event(self):
        return EventBase(self.name+"_end", self.end_year)

    def get_starting_event(self):
        return self.starting_event

    def get_ending_event(self):
        return self.ending_event
