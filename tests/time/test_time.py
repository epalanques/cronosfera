from cronosfera.time.time import Time
from cronosfera.time.time_manager import TimeManager

def test_comparison():
    periods = []

    fixed_period = Time("eon", "fixed_period", 7, 3)

    for i in range(9):
        periods.append(Time("eon", "period"+str(i), i+2, i))
    periods.append(Time("eon", "period"+str(10), 7, 3))

    assert fixed_period < periods[0]
    assert fixed_period < periods[1]
    assert fixed_period <= periods[2]
    assert fixed_period <= periods[3]
    assert fixed_period <= periods[4]
    assert fixed_period <= periods[5]
    assert fixed_period >= periods[6]
    assert fixed_period > periods[7]
    assert fixed_period > periods[8]
    assert fixed_period == periods[9]

    # Check t4

    for tested_period in periods:
        others = [tp for tp in periods if tp != tested_period]
        for other in others:
            if tested_period < other or tested_period <= other:
                assert not tested_period == other
                assert not tested_period > other
                assert not tested_period >= other
                if tested_period < other:
                    assert tested_period <= other
            elif tested_period == other:
                assert not tested_period < other
                assert not tested_period <= other
                assert not tested_period >= other
                assert not tested_period > other
            elif tested_period > other or tested_period >= other:
                assert not tested_period == other
                assert not tested_period < other
                assert not tested_period <= other
                if tested_period > other:
                    assert tested_period >= other


def test_contains():
    periods = []

    fixed_period = Time("eon", "fixed_period", 7, 3)

    for i in range(9):
        periods.append(Time("eon", "period" + str(i), i + 2, i))
    periods.append(Time("eon", "period" + str(10), 7, 3))

    containing_periods_index = [3, 4, 5, 9]
    for period in periods:
        if periods.index(period) in containing_periods_index:
            assert fixed_period.contains(period)
        else:
            assert not fixed_period.contains(period)


def test_overlaps():
    periods = []

    fixed_period = Time("eon", "fixed_period", 7, 3)

    for i in range(9):
        periods.append(Time("eon", "period" + str(i), i + 2, i))
    periods.append(Time("eon", "period" + str(10), 7, 3))

    overlapping_periods_index = [0, 1, 7, 8]
    for period in periods:
        if periods.index(period) in overlapping_periods_index:
            assert not period.overlaps(fixed_period)
        else:
            assert period.overlaps(fixed_period)


def test_add_period():

    manager = TimeManager()

    manager.add_period(Time("Supereon", "precambrian", 4600, 541))

    manager.add_period(Time("Eon", "Hadean", 4600, 4000))
    manager.add_period(Time("Eon", "Archean", 4000, 2500))
    manager.add_period(Time("Eon", "Proterozoic", 2500, 541))

    manager.add_period(Time("Era", "Eoarchean", 4000, 3600))
    manager.add_period(Time("Era", "Mesoarchean", 3200, 2800))

    precambrian = manager.get_period_by_name("precambrian")[1]

    assert [sp.name for sp in precambrian.sorted_subperiods()] == ["Hadean", "Archean",
                                                                   "Proterozoic"]

    assert precambrian.is_full()
    assert precambrian.sorted_subperiods()[1].name == "Archean"

    archean = manager.get_period_by_name("Archean")[1]
    assert not archean.is_full()
    assert "Eoarchean" in archean
    assert "Mesoarchean" in archean

    manager.add_period(Time("Era", "Paleoarchean", 3600, 3200))
    manager.add_period(Time("Era", "Neoarch", 2800, 2500))
    assert archean.is_full()
    assert "Paleoarchean" in archean

    try:
        manager.add_period(Time("Era", "TrollEra", 3500, 3000))
        assert False, "Didn't discard the overlapped era"
    except AssertionError:
        pass
