import pytest

from cronosfera.time import TimeManager

def pytest_addoption(parser):
    group = parser.getgroup('selenium', 'selenium')
    group._addoption('--headless',
                     action='store_true',
                     help='enable headless mode for supported browsers.'
                     )


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