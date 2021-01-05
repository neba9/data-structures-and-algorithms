print('proof of life')

# constructor to initialize the node object and create a new node class
class Node:
    # Function to initialize the head
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    
class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.start_node = None 

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node= new_node            

    # Function to inseret new data at the beginning
    def insert(self, new_data):
        new_data.next = self.start_node
        self.start_node = new_data

    def includes(self, item):
        current = self.start_node
        while current is not None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False

# utility function to print the linkedList
    def __str__(self):
        temp = self.start_node
        node_list = []
        node_print = ''
        while(temp):
            node_list.append(f'{ {temp.data} } -> ')
            temp = temp.next
            if temp == None:
                node_list.append('Null')
        for new_data in node_list:
            node_print += f'{new_data}'
        return node_print            
    
      
    