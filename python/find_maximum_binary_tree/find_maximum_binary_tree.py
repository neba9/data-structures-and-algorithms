# from tree.tree import Node
from tree.tree import Node, BinaryTree



def find_maximum_value(root):
  if (root == None):
    print('tree is empety')

  current = root.value
  left_value = find_maximum_value(left.value)
  right_value = find_maximum_value(right.value)

  if left_value > current:
    current = left_value
  if right_value > current:
    current = right_value
  return current


if __name__ == '__main__':
  root = Node(2)
  root.left = Node(7)
  root.right = Node(5)
  root.left.right = Node(6)
  root.left.right.left = Node(1)
  root.left.right.right = Node(11)
  root.right.right = Node(9)
  root.right.right.left = Node(6)
  print(find_maximum_value(root))
  
