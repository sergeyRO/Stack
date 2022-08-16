from queue import LifoQueue


class Stack(LifoQueue):
    # def __init__(self):
    #     ...

    def isEmpty(self):
        #True/False пустой или нет
        return self.empty()

    def push(self, a):
        #add Element
        self.put(a)

    def pop(self):
        #drop Element возвращает верхний элемент
        return self.get()

    def peek(self):
        #возвращает верхний элемент стека. Стек не меняется

        return self.get()

    def size(self):
        #возвращает количество элементов
        return self.qsize()

if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    stack.push(10)
    stack.push(5)
    stack.push(25)
    stack.push(2)
    print(stack.isEmpty())
    print(stack.size())
    print(stack.pop())
    print(stack.size())