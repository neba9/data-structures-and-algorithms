from linked_list.linked_list import LinkedList, Node

# def test_import():
#     assert LinkedList

# def test_empty_list():
#     actual = LinkedList().head
#     expected = None
#     assert actual == expected

# def test_insert():
#     ll = LinkedList()
#     ll.insert(5)
#     actual = ll.head.value
#     expected = 5
#     assert actual == expected

# def test_head_pointer():
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(3)
#     actual = ll.head.value
#     expected = 3
#     assert actual == expected

# def test_insert_multiple():
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(3)
#     actual = ll.head.value, ll.head.next.value, ll.head.next.next.value
#     expected = (3,2,1)
#     assert actual == expected

# def test_includes_true():
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(3)
#     actual = ll.includes(1)
#     expected = True
#     assert actual == expected

# def test_includes_false():
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(3)
#     actual = ll.includes(100)
#     expected = False
#     assert actual == expected

# def test_str_collection():
#     ll = LinkedList()
#     ll.insert('c')
#     ll.insert('b')
#     ll.insert('a')
#     actual = str(ll)
#     expected = "{a}->{b}->{c}->NULL"
#     assert actual == expected

# def test_append_single_end():
#     ll = LinkedList()
#     ll.append_node(2)
#     actual = str(ll)
#     expected = "{2}->NULL"
#     assert actual == expected

# def test_append_mullitple_end():
#     ll = LinkedList()
#     ll.append_node(3)
#     ll.append_node(4)
#     ll.append_node(5)
#     actual = str(ll)
#     expected = "{3}->{4}->{5}->NULL"
#     assert actual == expected












def test_import():
    assert LinkedList

link = LinkedList()

def test_empty_list():
    actual = link.insert(Node(None))
    expected = None
    assert actual == expected

def test_insert_list():
    actual = link.insert(Node(8))
    expected = None
    assert actual == expected

def test_head_link():
    actual = str(link)
    expected = '{8} -> {None} -> Null'
    assert actual == expected    

new_link = LinkedList()

def test_multiple_insert():
    new_link.insert(Node(a))
    new_link.insert(Node(b))
    new_link.insert(Node(c))
    actual = str(new_link)
    expected = '{c} -> {b} -> {a} -> Null'
    assert actual == expected 

def test_true_search():
    actual = new_link.includes(a)
    expected = True
    assert actual == expected 

def test_false_search():
    actual = new_link.includes('e')
    value = False  

def test_collection_of_all():
    actual = str(new_link)
    expected = '{c} -> {b} -> {a} -> Null'
    assert actual == expected

