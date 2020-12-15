# import pytest
from array_binary_search.array_binary_search  import binary_search

def test_binary_search():
  
    arr = [4,8,15,16,23,42]
    x = 15

    expected = 2
    actual = binary_search(arr,x)
    assert expected == actual

 


