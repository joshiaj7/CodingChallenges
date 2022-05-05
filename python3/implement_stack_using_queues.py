from collections import deque

# Space     : O(n)
# Push Time : O(1)
# Pop Time  : O(1)


class MyStack:

    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.appendleft(x)

    def pop(self) -> int:
        return self.dq.popleft()

    def top(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        return len(self.dq) == 0
