from Stack import Stack, StackBalance

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
    print(StackBalance().balance('[{}[][[]]]'))