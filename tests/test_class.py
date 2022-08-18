import pytest

from Stack import Stack

stack = Stack()

el = [(15),(25),(1),('A'),('S'),(101),(1)]

def test_isEmpty():
    assert stack.isEmpty() == True

@pytest.mark.parametrize("el", el)
def test_push(el):
    stack.push(el)
    assert stack.isEmpty() == False

    # res = app.add_doc(number_doc, type_doc, owner, shelf)
    # assert res == True