from cronosfera.events.event import Event
from cronosfera.events.event_base import EventBase
from random import randint


def test_punctual_event(time_manager):
    events = []
    for i in range(9):
        event = EventBase("ImportantEventBase"+str(i), randint(1000, 4600))
        events.append(event)
        time_manager.add_punctual_event(event)

    assert time_manager.get_events_by_period("ImportantEventBase1") == events[1]


def test_duration_event(time_manager):
    events = []
    for i in range(9):
        starting_year = randint(1541, 4600)
        ending_year = starting_year - randint(100, 1000)
        events.append(Event("ImportantEventBase"+str(i),starting_year, ending_year))

    for event in events:
        time_manager.add_duration_event(event)

    assert sorted(list(time_manager.get_events_by_period("precambrian").values())) == \
           sorted([event.get_starting_event() for event in events] + \
           [event.get_ending_event() for event in events])
