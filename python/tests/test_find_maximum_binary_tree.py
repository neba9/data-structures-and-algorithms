import pytest

from find_maximum_binary_tree.find_maximum_binary_tree import find_maximum_value
from find_maximum_binary_tree.tree import Node


def test_find_maximum_value():
  root = Node(2)
  root.left = Node(7)
  root.right = Node(5)
  root.left.right = Node(6)
  root.left.right.left = Node(1)
  root.left.right.right = Node(11)
  root.right.right = Node(9)
  root.right.right.left = Node(6)

  actual = find_maximum_value(root)
  expected = 11
  assert actual == expected
  


