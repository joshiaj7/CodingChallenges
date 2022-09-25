"""
Space   : O(n)
Time    : O(n)
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.k = k
        self.first = 0
        self.last = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.last = (self.last + 1) % self.k
        self.q[self.last] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.first == self.last:
            self.first, self.last = 0, -1
        else:
            self.first = (self.first + 1) % self.k
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.first]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.last]

    def isEmpty(self) -> bool:
        return self.last == -1

    def isFull(self) -> bool:
        return not self.isEmpty() and (self.last + 1) % self.k == self.first
