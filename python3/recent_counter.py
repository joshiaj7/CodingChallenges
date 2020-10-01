"""
space   : O(n)
time    : O(n)
"""


class RecentCounter:

    def __init__(self):
        self.history = []

    def ping(self, t: int) -> int:
        self.history.append(t)
        s = t - 3000

        while self.history[0] < s:
            self.history.pop(0)

        return len(self.history)
