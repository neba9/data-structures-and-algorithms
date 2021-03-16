from repeated_word.repeated_word import repeated_word

def test_repeated_word():
  actual = repeated_word('In good time in bad time friends are friends')
  expected = 'time'
  assert actual == expected