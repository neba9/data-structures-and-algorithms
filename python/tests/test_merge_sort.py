import pytest 
from merge_sort.merge_sort import merge_sort


def test_merge_sort():
  actual = merge_sort([8,4,23,42,16,15])
  expected = [4,8,15,16,23,42]
  assert actual == expected