
from .tree import Node, BinaryTree

def breadth_first(root):
  if (root == None):
    return 

# Create an empty queue and lists for breadth order traversal

  queue = []
  lists = []
  if root:
    queue.append(root)
  while (len(queue) > 0):
    current = queue.pop(0)
    lists.append(current.value)
    if current.left is not None:
      queue.append(current.left)
    
    if current.right is not None:
      queue.append(current.right)
  return lists



# if __name__ == '__main__':
#   root = Node(2)
#   root.left = Node(7)
#   root.right = Node(5)
#   root.left.right = Node(6)
#   root.left.right.left = Node(5)
#   root.left.right.right = Node(11)
#   root.right.right = Node(9)
#   root.right.right.left = Node(4)
#   root.left.left = Node(2)
#   root.left.right.right = Node(11)
#   print(breadth_first(root))
#   pass