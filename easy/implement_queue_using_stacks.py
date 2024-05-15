class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def transfer(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        self.transfer()
        return self.stack2.pop()

    def peek(self) -> int:
        self.transfer()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Runtime 25 ms / Memory 16.59 mb


# Example
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # Output: 1
print(queue.pop())  # Output: 1
print(queue.empty())  # Output: False
