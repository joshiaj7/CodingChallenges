from bisect import bisect_right

"""
Space : O(n)
Time  : O(log n)
"""


class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        lhs = bisect_right(self.calendar, start)

        if self.calendar and lhs < len(self.calendar) and ((lhs % 2) == 1 or self.calendar[lhs] < end):
            return False

        self.calendar.insert(lhs, end)
        self.calendar.insert(lhs, start)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
