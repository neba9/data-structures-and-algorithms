from insertion_sort.insertion_sort import insertion_sort
import pytest 

def test_insertion_sort():
  actual = insertion_sort([8,4,23,42,16,15])
  expected = [4,8,15,16,23,42]
  assert actual == expected