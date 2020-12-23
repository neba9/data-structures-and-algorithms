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

    def append_node(self, value):
        new_node = Node(value, next=None)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insert_before(self, value, newVal):
        current_node = self.head
        ll = LinkedList(current_node)
        if current_node.next is None:
            return "No Node Available"
        if ll.includes(value) is False:
            return "Value does not exist!"
        if current_node.value == value:
                current_node.next = Node(newVal, current_node.next)
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = Node(newVal, current_node.next)
            else:
                current_node = current_node.next

if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    # print(new_linked)

    new_linked1 = LinkedList(new_node)
    # print(new_linked1.head.value) # to see the value of 1

    # test insert method
    new_linked2 = LinkedList(new_node)
    new_linked2.insert(2) 
    new_linked2.insert(3) 
    new_linked2.insert(4) 
    new_linked2.insert(6) 
    # print(new_linked2.includes(3))
    new_linked2.insert_before(6, 5)
    print(new_linked2) # to see the value of inserted value 2

    # # test includes
    # new_linked1 = LinkedList(new_node)
    # new_linked1.insert(2) 
    # # print(new_linked1.includes(2))
    # # print(new_linked1.includes(5))
    # print(new_linked1.head.value) # to see if it includes values (boolean)

    # new_linked2 = LinkedList(new_node)
    # print(new_linked2.insert_before(1, 10))
    # print(new_linked2)    
     
    