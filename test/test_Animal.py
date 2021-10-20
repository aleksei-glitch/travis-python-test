import pytest
import Animal

def test_duck():
  a1 = Animal('duck', 'donald', 'quack')
  assert "The duck is named  \"donald\" and says \"quack\"." == a1.print_animal()
