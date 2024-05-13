from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
        return not self.q1 and not self.q2


c

# Example 1
# Input: ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output: [null, null, null, 2, 2, false]
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False
