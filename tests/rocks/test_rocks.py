
import pytest

from cronosfera.geology.earth.rocks.rock import Rock, RockManager


def test_add_subclass():
    rock = Rock("test")

    rock1 = rock.add_subclass("rock1")
    assert rock.subclassifications["rock1"]
    assert rock.subclassifications["rock1"].name == "rock1"
    assert rock1.name == "rock1"

    with pytest.raises(Exception):
        rock1.add_subclass(321)

    with pytest.raises(Exception):
        rock1.add_subclass(None)

    with pytest.raises(Exception):
        rock1.add_subclass(["rock1", "rock2"])

    with pytest.raises(Exception):
        rock1.add_other_names("rock1")


def test_add_other_names():
    rock1 = Rock("test1")
    rock2 = Rock('test2')

    rock1.add_other_names(["hi", "what's", "up"])

    with pytest.raises(Exception):
        rock1.add_other_names("what's")

    with pytest.raises(Exception):
        rock2.add_other_names(3)

    with pytest.raises(Exception):
        rock2.add_other_names(None)

    assert rock1.other_names == ["hi", "what's", "up"]
    assert rock2.other_names == []


def test_get_info():
    pass


def test_get_subclass():
    rock = Rock("test")

    for i in range(3):
        sub_class = rock.add_subclass("subtest%i" % i)
        sub_class.add_other_names(["subclass%i" % i,
                                   "minitest%i" % i,
                                   "type%i" % i])
    sub_subclass = rock.subclassifications["subtest2"].add_subclass("sub-subclass")
    sub_subclass.add_other_names(["tiny one", "deepest one"])

    assert rock.get_subclass("subtest1").name == "subtest1"
    assert rock.get_subclass("type2").name == "subtest2"

    assert not rock.get_subclass("sub-subclass")
    assert not rock.get_subclass("tiny one")

    subtest2 = rock.get_subclass("minitest2")
    assert subtest2.get_subclass("tiny one").name == "sub-subclass"
    assert subtest2.get_subclass("deepest one").name == "sub-subclass"

    assert not rock.get_subclass("test")
    assert not rock.get_subclass("type3")


def test_contains():
    rock = RockManager()

    for i in range(3):
        sub_class = rock.add_subclass("subtest%i" % i)
        sub_class.add_other_names(["subclass%i" % i,
                                   "minitest%i" % i,
                                   "type%i" % i])

    assert "subtest1" in rock
    assert "type2" in rock
    assert "subtest2" in rock
    assert "subtest0" in rock

    assert "type4" not in rock
    assert "test" not in rock


def test_create_full_path():
    rock = RockManager()

    rock.create_full_path('path/to/subtest')
    rock.create_full_path('path/to/subtest2')
    rock.create_full_path('path/to/another/subtest')

    assert list(rock.subclassifications.keys()) == ["path"]

    path = rock.subclassifications["path"]
    assert list(path.subclassifications.keys()) == ["to"]

    path_to = path.subclassifications["to"]
    assert sorted(list(path_to.subclassifications.keys())) == sorted(["subtest",
                                                                      "subtest2",
                                                                      "another"])

    subset = path_to.subclassifications["subtest"]
    assert list(subset.subclassifications.keys()) == []

    subset2 = path_to.subclassifications["subtest2"]
    assert list(subset2.subclassifications.keys()) == []

    another = path_to.subclassifications["another"]
    assert list(another.subclassifications.keys()) == ["subtest"]

    another_subset = another.subclassifications["subtest"]
    assert list(another_subset.subclassifications.keys()) == []


def test_get_rock():
    rock = RockManager()

    rock.create_full_path('path/to/subtest')
    rock.create_full_path('path/to/subtest2')
    rock.create_full_path('path/to/another/subtest')

    assert rock.get_rock('subtest').name == 'subtest'
    assert rock.get_rock('to').name == 'to'
    assert rock.get_rock('path').name == 'path'
    assert not rock.get_rock("Not added rock")
    assert not rock.get_rock("NeitherThisOne")
