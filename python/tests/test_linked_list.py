from linked_list.linked_list import LinkedList, Node

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

def test_append_single_end():
    ll = LinkedList()
    ll.append_node(2)
    actual = str(ll)
    expected = "{2}->NULL"
    assert actual == expected

def test_append_mullitple_end():
    ll = LinkedList()
    ll.append_node(3)
    ll.append_node(4)
    ll.append_node(5)
    actual = str(ll)
    expected = "{3}->{4}->{5}->NULL"
    assert actual == expected