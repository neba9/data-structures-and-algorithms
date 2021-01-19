
import pytest
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_multi_bracket_validation():
  expr = multi_bracket_validation('{}(){}')
  actual = expr
  expected = True
  assert actual == expected
  
def test_multi_bracket_validation():
  expr = multi_bracket_validation('{(})')
  actual = expr
  expected = False
  assert actual == expected



