class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        #True/False пустой или нет
        if len(self.stack) > 0:
            return False
        else:
            return True

    def push(self, a):
        #add Element
        return self.stack.append(a)

    def pop(self):
        #drop Element возвращает верхний элемент
        return self.stack.pop()

    def peek(self):
        #возвращает верхний элемент стека. Стек не меняется
        if not self.isEmpty():
            return self.stack[len(self.stack)-1]
        else:
            return None

    def size(self):
        #возвращает количество элементов
        return len(self.stack)

    def balance(self, parentheses):
        self.stack.clear()
        if len(parentheses)%2 != 0:
            return "Несбалансированно"
        else:
            for item in parentheses:
                if stack.peek() == '{' and item == '}':
                    stack.pop()
                elif stack.peek() == '[' and item == ']':
                    stack.pop()
                elif stack.peek() == '(' and item == ')':
                    stack.pop()
                else:
                    stack.push(item)
            if stack.isEmpty():
                return "Сбалансированны"
            else:
                return "Несбалансированны"

if __name__ == '__main__':
    #Для задания №1
    stack = Stack()
    print(stack.isEmpty())
    stack.push(10)
    stack.push(5)
    stack.push(25)
    stack.push(2)
    print(stack.isEmpty())
    print(stack.size())
    print(stack.pop())
    print(stack.peek())

    #Для задания №2
    print(stack.balance('[{[{(()])}}]'))