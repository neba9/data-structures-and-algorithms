import pytest
from fizz_buzz_tree.tree import Node,BinaryTree,BinarySearchTree

# from tree.tree import Node,BinaryTree,BinarySearchTree

def test_add_single():
  tree = BinarySearchTree()
  tree.add(20)
  actual = tree.root.value
  expected = 20
  assert actual == expected

def test_add_le_ri():
  tree = BinarySearchTree()
  tree.add(20)
  tree.add(15)
  tree.add(25)
  actual = tree.root.value
  actual = tree.root.left.value
  actual = tree.root.right.value
  expected = 20
  expected = 15
  expected = 25
  assert actual == expected

def test_pre_order():
  # a = Node("A")
  b = Node("B")
  c = Node("C")

  tree = BinaryTree(Node("A"))
  tree.root.left = b
  tree.root.right = c

  actual = tree.root.value
  actual = tree.root.left.value
  actual = tree.root.right.value

  expected = 'A'
  expected = 'B'
  expected = 'C'

  assert actual == expected

def test_in_order():
  # a = Node("A")
  b = Node("B")
  c = Node("C")

  tree = BinaryTree(Node("A"))
  tree.root.left = b
  tree.root.right = c

  actual = tree.root.value
  actual = tree.root.left.value
  actual = tree.root.right.value

  expected = 'B'
  expected = 'A'
  expected = 'C'

  assert actual == expected

def test_post_order():
  # a = Node("A")
  b = Node("B")
  c = Node("C")

  tree = BinaryTree(Node("A"))
  tree.root.left = b
  tree.root.right = c

  actual = tree.root.value
  actual = tree.root.left.value
  actual = tree.root.right.value

  expected = 'B'
  expected = 'C'
  expected = 'C'

  assert actual == expected

 
