"""
space   : O(n)
time    : O(n)
"""


class RecentCounter:

    def __init__(self):
        self.history = []

    def ping(self, t: int) -> int:
        s = t - 3000
        calls = 0

        self.history.append(t)
        n = len(self.history)

        for i in range(n-1, -1, -1):
            if s <= self.history[i]:
                calls += 1
            else:
                break

        return calls
