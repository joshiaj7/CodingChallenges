import math

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start, end = 0, math.floor(math.sqrt(c))

        while start <= end:
            cal = (start * start) + (end * end)
            if cal == c:
                return True

            if cal > c:
                end -= 1
            else:
                start += 1

        return False
