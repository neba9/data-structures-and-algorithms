import pytest

from find_maximum_binary_tree.tree import Node, BinaryTree
from fizz_buzz_tree.fizz_buzz_tree import fizz_buzz, fizz_buzz_tree
# @pytest.fixture
# def fizzy_tree():
#     ## preparing data
#     tree = BinaryTree()
#     tree.root = Node(3)
#     tree.root.left = Node(5)
#     tree.root.right = Node(7)
#     tree.root.left.left = Node(15)

#     return tree


def test_fizz_buzz_tree():
  bt = BinaryTree()
  bt.root = Node(3)
  actual = fizz_buzz_tree()
  expected = 'Fizz'
  assert actual == expected

# def test_fizz_buzz_five():
#   tree = BinaryTree()
#   tree.root = Node(5)
#   actual = fizz_buzz_tree()
#   expected = 'Buzz'
#   assert actual == expected

# def test_fizz_buzz_fifteen():
#   tree = BinaryTree()
#   tree.root = Node(15)
#   actual = fizz_buzz_tree()
#   expected = 'FizzBuzz'
#   assert actual == expected







# tree.root = Node(3)
# tree.root.left = Node(5)
# tree.root.right = Node(7)
# tree.root.left.left =Node(15)
# print(fizz_buzz_tree(tree))

# actual = find_maximum_value(root)
# expected = 11
# assert actual == expected