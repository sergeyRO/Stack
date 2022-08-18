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
        if len(parentheses)%2 != 0:
            return "Несбалансированно"
        else:
            for item in parentheses:
                if self.peek() == '{' and item == '}':
                    self.pop()
                elif self.peek() == '[' and item == ']':
                    self.pop()
                elif self.peek() == '(' and item == ')':
                    self.pop()
                else:
                    self.push(item)
            if self.isEmpty():
                return "Сбалансированны"
            else:
                return "Несбалансированны"