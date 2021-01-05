from linked_list.linked_list import LinkedList, Node

# utility function to print the linkedList & Inserts a new Node at front of the list  
def append_data(self):
    # Allocate the Node & Put in the data 
  new_node = self.Node(new_data)
    #  Make next of new Node as head 
  new_node.next = self.start_node
    # Move the head to point to new Node 
  self.start_node = new_node

def zip_lists(list1, list2):
  list1_current = list1.start_node
  list2_current = list2.start_node
  # while there are avalable postions in list1
  while list1 != None and list2 != None:
    # save next pointer
    list1_next = list1_current.next
    list2_next = list2_current.next

    # update current pointer for next itration
    list1_current = list1_next
    list2_current = list2_next
  list2.start_node = list2_current  

def __str__(self): 
    temp = self.start_node 
    while temp != None: 
        print(temp.new_data), 
        temp = temp.next
    print('') 
     

# if __name__ == "__main__"
llist1 = LinkedList()
llist2 = LinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(2)
print(llist1)