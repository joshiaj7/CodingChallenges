"""
Space   : O(1)
Time    : O(log n)
where n is the discrepancy of X and Y
"""


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while Y > X:
            if Y % 2 == 1:
                Y += 1
                ans += 1

            Y //= 2
            ans += 1

        return ans + (X - Y)
