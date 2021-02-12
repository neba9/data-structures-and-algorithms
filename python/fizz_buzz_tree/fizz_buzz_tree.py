# from find_maximum_binary_tree.tree import Node, BinaryTree
from .tree import Node, BinaryTree, BinarySearchTree

def fizz_buzz(value):
  if value % 15 == 0:
    return 'FizzBuzz'
  if value % 3 == 0:
    return 'Fizz'
  if value % 5 == 0:
    return 'Buzz'
  else:
    return str(value)



def fizz_buzz_tree(starting_tree):
  
  tree = BinaryTree()
  # new_nodes = Node(fizz_buzz(current.value))
  def check_node(current):
    new_nodes = Node()
    new_nodes.value = Node(fizz_buzz(current.value))
    if current.left:
      new_nodes = check_node(current.root.left)
    if current.right:
      new_nodes.right = check_node(current.root.right)
    return new_nodes
  tree.root = check_node(tree.root)
  return tree




# if __name__ == '__main__':
# #   tree = BinaryTree()
# #   tree.root = Node(3)
# #   tree.root.left = Node(5)
# #   tree.root.right = Node(7)
# #   tree.root.left.left = Node(15)
# #   print(fizz_buzz_tree(tree))

#   binary_tree = BinaryTree(Node(2))
#   binary_tree.root.left = Node(5)
#   binary_tree.root.right = Node(3)
#   print(fizz_buzz_tree(binary_tree))


