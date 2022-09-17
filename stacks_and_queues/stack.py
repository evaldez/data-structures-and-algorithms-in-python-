from dataclasses import dataclass

#@dataclass
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length == 0 : return Node(None)
        return self.top

    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.top = node
            self.bottom = node
        else:
            current_top_node = self.top
            self.top = node
            self.top.next = current_top_node
        self.length += 1
        return

    def pop(self):
        if self.length == 0:
            return None

        current_node = self.top
        self.top = self.top.next
        self.length -= 1

        return current_node
        
    def isEmpty(self):
        if self.length == 0: return True
        return False
            

if __name__ == '__main__':
    stack = Stack()
    print(f'is empty {stack.isEmpty()} ' )
    stack.push('number1')
    stack.push('number2')
    stack.push('number3')
    stack.push('number4')
    print(stack.peek().value)
    popped_value = stack.pop()
    print(f'popped_value1: {popped_value.value} ')
    print(stack.peek().value)
    stack.push('final')
    print(stack.peek().value)
    popped_value = stack.pop()
    popped_value = stack.pop()
    print(f'is empty {stack.isEmpty()} ' )