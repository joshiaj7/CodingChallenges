from collections import defaultdict
from bisect import insort

"""
Space   : O(n)
Time    : O(n log n)
"""


class MyCalendarThree:

    def __init__(self):
        self.times = defaultdict(int)
        self.values = []

    def book(self, start: int, end: int) -> int:
        self.times[start] += 1
        self.times[end] -= 1
        insort(self.values, start)
        insort(self.values, end)

        prev = -1
        events_on = 0
        ans = 0
        for i in self.values:
            if prev == i:
                continue
            prev = i
            events_on += self.times[i]
            ans = max(ans, events_on)

        return ans
