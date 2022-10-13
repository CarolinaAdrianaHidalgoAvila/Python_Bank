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

def test_quicksort_4_a():
    resp = quicksort(array=[1,2,3])
    assert  resp==[1,2,3]

def test_quicksort_4_b():
    resp = quicksort(array=[2,1,3])
    assert  resp==[1,2,3]

#bubblesort

def test_bubbleSort_a():
    resp = bubbleSort(theSeq=[])
    assert resp==[]

def test_bubbleSort_b():
    resp = bubbleSort(theSeq=[1])
    assert resp==[1]

def test_bubbleSort_c():
    resp = bubbleSort(theSeq=[1,2])
    assert resp==[1,2]

def test_bubbleSort_d():
    resp = bubbleSort(theSeq=[1,2,3])
    assert resp==[1,2,3]

def test_bubbleSort_e():
    resp = bubbleSort(theSeq=[2,1,3])
    assert resp==[1,2,3]