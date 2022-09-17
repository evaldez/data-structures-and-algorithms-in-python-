from dataclasses import dataclass

class Stack:
    def __init__(self):
        self.list = []

    def peek(self):
        if len(self.list) == 0 : return None
        return self.list[-1]

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
        
    def isEmpty(self):
        if len(self.list) == 0: return True
        return False
            

if __name__ == '__main__':
    stack = Stack()
    print(f'is empty {stack.isEmpty()} ' )
    stack.push('number1')
    stack.push('number2')
    stack.push('number3')
    stack.push('number4')
    print(stack.peek())
    popped_value = stack.pop()
    print(f'popped_value1: {popped_value} ')
    print(stack.peek())
    popped_value = stack.pop()
    popped_value = stack.pop()
    stack.push('final')
    print(stack.peek())
    popped_value = stack.pop()
    popped_value = stack.pop()
    print(f'is empty {stack.isEmpty()} ' )