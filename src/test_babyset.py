# test_babyset.py
# Demonstrates unit testing using the pytest module.
# pytest must be installed through pip.
# py.test to run
# use triple quotes for documentation
# pydoc ./src/baby_set.py  or  pydoc -w ./src/baby_set.py   will generate a html file
import pytest
from baby_set import BabySet

def test_init():
    bset = BabySet([2, 4, 4])
    assert bset.size() == 2

def test_init_empty():
    bset = BabySet()
    assert bset.size() == 0

def test_add():
    bset = BabySet([2, 4, 4])
    bset.add(4)
    assert bset.size() == 2

def test_addSeq():
    bset = BabySet([2, 4, 4])
    bset.addSeq([4, 5, 6, 7])
    assert bset.size() == 5

def test_get():
    bset = BabySet([2, 4, 4])
    with pytest.raises(KeyError):
      bset.get(7)

def test_remove():
    bset = BabySet([2, 4, 4])
    with pytest.raises(KeyError):
       bset.remove(6)

def test_clear():
    bset = BabySet([2, 4, 4])
    bset.clear()
    assert bset.size() == 0
