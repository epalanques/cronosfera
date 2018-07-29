
TIME_ORDER = ['manager', 'supereon', 'eon', 'era', 'periodo', 'epoca', 'edad', 'cron']


class Time(object):
    def __init__(self, period_type, name, starting_year, end_year):
        self.name = name

        period_type = period_type.lower()
        assert period_type in TIME_ORDER, 'time period not recognized'
        self.type = period_type

        assert end_year < starting_year, "End year must be later than starting year"
        self.starting_year = starting_year
        self.end_year = end_year

        self.subperiods = {}
        self.events = {}

    def __lt__(self, other):
        return self.end_year >= other.starting_year

    def __le__(self, other):
        cond1 = self.starting_year > other.starting_year
        cond2 = self.starting_year == other.starting_year and self.end_year < other.end_year
        return cond1 or cond2

    def __eq__(self, other):
        return other.starting_year == self.starting_year and other.end_year == self.end_year

    def __ne__(self, other):
        return other.starting_year != self.starting_year or other.end_year != self.end_year

    def __ge__(self, other):
        cond1 = self.starting_year < other.starting_year
        cond2 = self.starting_year == other.starting_year and self.end_year > other.end_year
        return cond1 or cond2

    def __gt__(self, other):
        return self.starting_year <= other.end_year

    def __str__(self):
        return self.name

    def __contains__(self, item):
        try:
            return item in self.subperiods.values()
        except AttributeError:
            return item in self.subperiods.keys()


    def contains(self, other):
        try:
            cond1 = self.starting_year >= other.starting_year >= self.end_year
            cond2 = self.starting_year >= other.end_year >= self.end_year
            return cond1 and cond2
        except AttributeError:
            return self.starting_year >= other.year >= self.end_year

    def overlaps(self, other):
        cond1 = other.starting_year > self.starting_year > other.end_year
        cond2 = other.starting_year > self.end_year > other.end_year
        cond3 = other == self
        return cond1 or cond2 or cond3

    def is_final(self):
        return not self.subperiods

    def is_full(self):
        subperiods = self.sorted_subperiods()

        cond1 = subperiods[0].starting_year == self.starting_year
        if not cond1:
            # todo: Create a warning, not just print
            print("Empty period at the beggining: %s - %s"
                  % (str(self.starting_year), str(subperiods[0].starting_year)))

        cond2 = True
        for i in range(len(self.subperiods)-1):
            if subperiods[i].end_year != subperiods[i+1].starting_year:
                cond2 = False
                print("Empty period between %s (%s) and %s (%s)"
                      % (subperiods[i].name, str(subperiods[i].end_year),
                         subperiods[i+1].name, str(subperiods[i+1].starting_year)))

        cond3 = subperiods[-1].end_year == self.end_year
        if not cond3:
            print("Empty period at the end: %s - %s"
                  % (str(subperiods[-1].end_year), str(self.end_year)))

        return cond1 and cond2 and cond3

    def sorted_subperiods(self):
        return sorted(self.subperiods.values())

    def subperiod_type(self):
        for i in range(len(TIME_ORDER)):
            if TIME_ORDER[i] == self.type:
                return TIME_ORDER[i+1]

    def add_period(self, new_period):
        # The new period is immediately contained in the current period

        if self.subperiod_type() == new_period.type:
            for subperiod in self.subperiods.values():
                assert not subperiod.overlaps(new_period), "%s overlaps %s" \
                                                           % (new_period.name, subperiod.name)
            self.subperiods[new_period.name] = new_period
        else:
            containing_period = [subperiod for subperiod in self.subperiods.values()
                                 if subperiod.contains(new_period)]
            assert containing_period, "No period contains %s" % new_period.name
            containing_period[0].add_period(new_period)

    def get_period_by_name(self, period_name):
        if self.name == period_name:
            return self

        else:
            if self.is_final():
                return
            else:
                for subperiod in self.subperiods.values():
                    period = subperiod.get_period_by_name(period_name)
                    if period:
                        return period
                return

    def get_period_by_year(self, year, period_type='edad'):
        if self.is_final():
            return
        else:
            if self.contains(year) and self.type == 'edad':
                return self
            else:
                for subperiod in self.subperiods.values():
                    period = subperiod.get_period_by_year(year, period_type)
                    if period:
                        return period
                return

    def add_punctual_event(self, event):
        for subperiod in self.subperiods.values():
            if subperiod.contains(event):
                subperiod.events[event.name] = event
                subperiod.add_punctual_event(event)
                return
        return

    def add_duration_event(self, event):
        self.add_punctual_event(event.get_starting_event())
        self.add_punctual_event(event.get_ending_event())

    def get_events_by_period(self, period_name):
        return list(self.get_period_by_name(period_name).events.keys())

    def get_event_period(self, event_name, period_type):
        event_times = []
        for subperiod in self.subperiods.values():
            if subperiod.type == period_type:
                if event_name in [event.name for event in subperiod.events]:
                    event_times.append(subperiod.name)
            else:
                times = subperiod.get_event_time(event_times, period_type)
                event_times = event_times + times
        return event_times
