import stack

class MyQueue:

    def __init__(self):
        self.stack = []
        return

    def push(self, x: int) -> None:
        self.stack.append(x)
        return

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if len(self.stack): 
            return False
        else:
            return True


if __name__ == '__main__':
    queue = MyQueue()
    print(f'is empty {queue.empty()} ' )
    queue.push('1')
    queue.push('2')
    print(f'queue.peek().value {queue.peek()} ' )
    print(f'popd_value: {queue.pop()} ')
    print(f'is empty {queue.empty()} ' )


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()