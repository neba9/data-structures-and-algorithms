from tree import Node

class BinaryTree:
    def __init__(self):
        self.root = None 

    def pre_order(self):
        
        new_value = []
        def traverse(node):
            new_value.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return new_value

def tree_intersection(tree_1,tree_2):
   
    value_1 = tree_1.pre_order()
    value_2 = tree_2.pre_order()
    common_values = []
    for i in value_1:
        for j in value_2:
            if i == j:
                common_values.append(i)

    return set(common_values)

    
if __name__ == "__main__":
    tree_1 = BinaryTree()
    tree_1.root = Node(150)
    tree_1.root.right = Node(250)
    tree_1.root.left = Node(100)
    tree_1.root.left.left = Node(75)
    tree_1.root.right.left = Node(200)
    tree_1.root.right.right = Node(350)
    tree_1.root.left.right = Node(160)

    tree_2 = BinaryTree()
    tree_2.root = Node(42)
    tree_2.root.right = Node(600)
    tree_2.root.left = Node(100)
    tree_2.root.left.left = Node(15)
    tree_2.root.left.right = Node(160)
    tree_2.root.right.left = Node(200)
    tree_2.root.right.right = Node(350)

    print(tree_intersection(tree_1,tree_2)) 







