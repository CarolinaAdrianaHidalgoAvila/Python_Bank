import pytest
from Code.SortingAlgorithms.QuickSort import quicksort
from Code.SortingAlgorithms.BubbleSort import bubbleSort



def test_quicksort():
    resp = quicksort(array=[])
    assert resp==[]

def test_quicksort_2():
    resp = quicksort(array=[1])
    assert resp==[1]

def test_quicksort_3():
    resp = quicksort(array=[1,2])
    assert resp==[1,2]

def test_quicksort_4():
    resp = quicksort(array=[1,2,3])
    assert  resp==[1,2,3]

def test_quicksort_4():
    resp = quicksort(array=[2,1,3])
    assert  resp==[1,2,3]

#bubblesort

def test_bubbleSort():
    resp = bubbleSort(theSeq=[])
    assert resp==[]

def test_bubbleSort():
    resp = bubbleSort(theSeq=[1])
    assert resp==[1]

def test_bubbleSort():
    resp = bubbleSort(theSeq=[1,2])
    assert resp==[1,2]

def test_bubbleSort():
    resp = bubbleSort(theSeq=[1,2,3])
    assert resp==[1,2,3]

def test_bubbleSort():
    resp = bubbleSort(theSeq=[2,1,3])
    assert resp==[1,2,3]