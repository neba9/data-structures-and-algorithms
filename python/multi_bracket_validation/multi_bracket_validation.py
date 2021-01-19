

def multi_bracket_validation(input):
  """
  """
  opening = tuple('({[')
  closing = tuple(')}]')
  mapping = dict(zip(opening, closing))

  new_tuple = []
  # print(mapping['('])
  for expression in input :
    if expression in opening:
      new_tuple.append(mapping[expression])
    elif expression in closing:
      if not (new_tuple) or (expression != new_tuple.pop()):
        return False
  return not new_tuple

if __name__ == '__main__':
  o=multi_bracket_validation('{}(){}')
  m=multi_bracket_validation('{(})')
  print(o)
  print(m)
