from dataclasses import dataclass

#@dataclass
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length == 0 : return Node(None)
        return self.last

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            current_last_node = self.last
            self.last.next = node
            self.last = node

        self.length += 1
        return

    def dequeue(self):
        if self.length == 0:
            return None

        current_first_node = self.first
        self.first = current_first_node.next
        self.length -= 1

        return current_first_node
        
    def isEmpty(self):
        if self.length == 0: return True
        return False
            

if __name__ == '__main__':
    queue = Queue()
    print(f'is empty {queue.isEmpty()} ' )
    queue.enqueue('number1')
    queue.enqueue('number2')
    queue.enqueue('number3')
    queue.enqueue('number4')
    queue.enqueue('number5')
    queue.enqueue('number6')
    print(f'queue.peek().value: {queue.peek().value} ')
    print(f'dequeued_value: {queue.dequeue().value} ')
    print(f'dequeued_value: {queue.dequeue().value} ')
    print(f'queue.peek().value {queue.peek().value} ' )
    queue.enqueue('final')
    print(f'queue.peek().value {queue.peek().value} ' )
    print(f'dequeued_value: {queue.dequeue().value} ')
    print(f'dequeued_value: {queue.dequeue().value} ')
    print(f'is empty {queue.isEmpty()} ' )