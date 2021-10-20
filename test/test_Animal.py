import pytest
from Animal import Animal

def test_duck():
  a1 = Animal('duck', 'donald', 'quack')
  testStr = a1.print_animal()
  assert testStr == 'The duck is named  donald and says quack.'
