import pytest
from Code.SortingAlgorithms.QuickSort import quicksort

def test_changePreferredInvestment():
    costumerStart = quicksort(array=[])
    assert costumerStart==[]

def test_changePreferredInvestment():
    costumerStart = quicksort(array=[1])
    assert costumerStart==[1]

def test_changePreferredInvestment():
    costumerStart = quicksort(array=[1,2])
    assert costumerStart==[1,2]

def test_changePreferredInvestment():
    costumerStart = quicksort(array=[1,2,3])
    assert not costumerStart==[1,2,3]