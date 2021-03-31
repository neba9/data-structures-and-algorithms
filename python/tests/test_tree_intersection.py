# from find_maximum_binary_tree.tree import Node
# from fizz_buzz_tree.tree import Node

# from tree_intersection.tree_intersection import BinaryTree, tree_intersection, Node

# def test_tree_intersection():
#   tree_1 = BinaryTree()
#   tree_1.root = Node(150)
#   tree_1.root.right = Node(250)
#   tree_1.root.left = Node(100)
#   tree_1.root.left.left = Node(75)
#   tree_1.root.right.left = Node(200)
#   tree_1.root.right.right = Node(350)
#   tree_1.root.left.right = Node(160)

#   tree_2 = BinaryTree()
#   tree_2.root = Node(42)
#   tree_2.root.right = Node(600)
#   tree_2.root.left = Node(100)
#   tree_2.root.left.left = Node(15)
#   tree_2.root.left.right = Node(160)
#   tree_2.root.right.left = Node(200)
#   tree_2.root.right.right = Node(350)

#   actual = (tree_intersection(tree_1,tree_2))
#   expected = {160, 100, 350, 200}
#   assert actual == expected