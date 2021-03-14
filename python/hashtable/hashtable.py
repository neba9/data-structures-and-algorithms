from hashtable.linked_list import LinkedList

class Hashtable:

  def  __init__(self, size=1024):
    self.size = size
    self._buckets = size * [None]

  def _hash(self, key):
    sum = 0

    for ch in key:
      sum += ord(ch)

    primed = sum * 19

    index = primed % self.size

    return index

  def add(self, key, value):

    hashed_key_index = self._hash(key)

    if not self._buckets[hashed_key_index]:
      self._buckets[hashed_key_index] = LinkedList()

    self._buckets[hashed_key_index].add((key, value))

  def get(self, requested_ket):

    hashed_key_index = self._hash(requested_ket)

    if self._buckets[hashed_key_index]:
      return self._buckets[hashed_key_index].get(requested_ket)[1]
    return 'null'

  def contains(self, requested_ket):
    
    hashed_key_index = self._hash(requested_ket)

    if self._buckets[hashed_key_index]:
      return self._buckets[hashed_key_index].includes(requested_ket)

    else:
      return False


