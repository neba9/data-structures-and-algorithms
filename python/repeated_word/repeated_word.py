# from hashtable.hashtable import Hashtable


def repeated_word(str):
  """
  set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set. 
  """
  temp = set()

  for word in str.split():
    if word in temp:
      return word
    else:
      temp.add(word)
      
  return 'not repeated word'




