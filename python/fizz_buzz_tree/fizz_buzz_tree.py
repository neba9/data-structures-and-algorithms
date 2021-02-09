from find_maximum_binary_tree.tree import Node, BinaryTree, BinarySearchTree

def fizz_buzz(value):
  if value % 15 == 0:
    return 'FizzBuzz'
  if value % 3 == 0:
    return 'Fizz'
  if value % 5 == 0:
    return 'Buzz'
  else:
    return str(value)

def fizz_buzz_tree():
  new_tree = BinaryTree()
  # new_node = Node()
  if tree.root == None:
    return new_tree

  def check_node(current):
    new_nodes = Node(fizz_buzz(current.value))
    if current.left:
      new_nodes = check_node(current.left)
    if current.right:
      new_nodes.right = check_node(current.right)
    return new_nodes
  new_tree.root = check_node(tree.root)

  return new_tree




if __name__ == '__main__':
  tree = BinaryTree()
  tree.root = Node(3)
  tree.root.left = Node(5)
  tree.root.right = Node(7)
  tree.root.left.left =Node(15)
  # print(fizz_buzz_tree(tree))

  # root = Node(2)
  # root.left = Node(7)
  # root.right = Node(5)
  # root.left.right = Node(6)
  # root.left.right.left = Node(1)
  # root.left.right.right = Node(11)
  # root.right.right = Node(9)
  # root.right.right.left = Node(6)
  # print(find_maximum_value(root))
  # pass 