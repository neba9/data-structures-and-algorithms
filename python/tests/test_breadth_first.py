import pytest

from breadth_first.breadth_first import breadth_first
from breadth_first.tree import Node




def breadth_first():
  root = Node(2)
  root.left = Node(7)
  root.right = Node(5)
  root.left.right = Node(6)
  root.left.right.left = Node(5)
  root.left.right.right = Node(11)
  root.right.right = Node(9)
  root.right.right.left = Node(4)
  root.left.left = Node(2)
  root.left.right.right = Node(11)
  # print(breadth_first(root))

  actual = breadth_first(root)
  expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
  assert actual == expected