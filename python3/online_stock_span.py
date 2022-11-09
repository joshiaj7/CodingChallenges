"""
Space   : O(n)
Time    : O(n)
"""


class StockSpanner:
    def __init__(self):
        self.stack = [[float('inf'), 0]]

    def next(self, price: int) -> int:
        currDay = self.stack[-1][1] + 1

        while price >= self.stack[-1][0]:
            self.stack.pop()

        ans = currDay - self.stack[-1][1]
        self.stack.append([price, currDay])

        return ans
