import pytest

from cronosfera.time import TimeManager


@pytest.yield_fixture(scope="function")
def time_manager():
    manager = TimeManager()

    manager.add_period(manager.create_period("Supereon", "precambrian", 4600, 541))

    manager.add_period(manager.create_period("Eon", "Hadean", 4600, 4000))
    manager.add_period(manager.create_period("Eon", "Archean", 4000, 2500))
    manager.add_period(manager.create_period("Eon", "Proterozoic", 2500, 541))

    manager.add_period(manager.create_period("Era", "Eoarchean", 4000, 3600))
    manager.add_period(manager.create_period("Era", "Mesoarchean", 3200, 2800))

    yield manager
