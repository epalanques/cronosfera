
class EventBase:

    def __init__(self, name, year):
        self.name = name
        self.year = year

        self.location = None
        self.discovery_locatation = None

        self.short_description = None
        self.long_description = None

    def add_short_description(self, short_description):
        self.short_description = short_description

    def add_long_description(self, long_description):
        self.long_description = long_description

    def add_location(self, location):
        self.location = location

    def add_discovery_location(self, discovery_location):
        self.discovery_locatation = discovery_location

    def __lt__(self, other):
        return self.year > other.year

    def __le__(self, other):
        return self.year >= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ge__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year < other.year
