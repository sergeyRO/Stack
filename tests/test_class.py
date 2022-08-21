import pytest

from Stack import Stack

stack = Stack()

el = [(15),(25),(1),('A'),('S'),(101),(1)]
balance = [('{[(({[]}))]}'),('{[(({[}))]}'),('{[(({[[[]}))]}')]

def test_isEmpty():
    assert stack.isEmpty() == True

@pytest.mark.parametrize("el", el)
def test_push(el):
    stack.push(el)
    assert stack.isEmpty() == False

def test_pop():
    assert stack.pop() == 1

def test_peek():
    assert stack.peek() == 101

def test_size():
    assert stack.size() == 6

@pytest.mark.parametrize("balance", balance)
def test_balance(balance):
    b = stack.balance(balance)
    if b == 'Сбалансированны':
        assert b == 'Сбалансированны'
    else:
        assert b == 'Несбалансированны'