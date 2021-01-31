class Node:
    ''' We need to point to two other nodes ina a Binary Tree so the Node must have two pointers
        Traditionally they are called 'left' and 'right'
    '''
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    
    def pre_order(self):
        def traverse(root):
            # print root first
            print(root.value)
            # traverse left second
            if root.left:
                traverse(root.left)
            # traverse right last
            if root.right:
                traverse(root.right)
        traverse(self.root)

    
    def in_order(self):
        def traverse(root):
            # traverse left first
            if root.left:
                traverse(root.left)
            # operate on root second
            print(root.value)
            # traverse right last
            if root.right:
                traverse(root.right)
        traverse(self.root)

    def post_oredr(self):
      def traverse(root):
        #traverse left first
        if root.left:
          traverse(root.left)
        #traverse on right child
        if root.right:
          traverse(root.right)
        print(root.value)
        #print the data of node or print the root last
      traverse(self.root)
     

class BinarySearchTree(BinaryTree):
  def add(self, value):
    #find the correct spot to add this value and add it there
    pass

  def contains(self, value):
    #return true if the value is in the tree or false otherwise
    pass



if __name__ == "__main__":
    # Set a as root
    # set left of a to b
    # set the right of a to c


    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")

    b.left = d
    b.right = e
    c.left = f
# Option 1
    tree = BinaryTree()
    # print(tree)

    # a.left = b
    # a.right = c
    # tree.root = a
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)
# option 2
    tree = BinaryTree(Node("A"))
    tree.root.left = b
    tree.root.right = c
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)
    # print(tree.root.left.left.value)
    
    # tree.in_order()
    # tree.pre_order()
    # tree.post_oredr()

