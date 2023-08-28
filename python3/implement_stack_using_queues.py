from collections import deque

"""
Space     : O(n)
Push Time : O(n)
Pop Time  : O(1)
"""

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        temp = deque([x])
        temp.extend(self.queue)
        self.queue = temp

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
        