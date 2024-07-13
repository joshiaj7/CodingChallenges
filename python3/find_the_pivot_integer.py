"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = 0
        for i in range(1, n+1):
            total += i

        left, right = 0, total
        for i in range(1, n+1):
            left += i
            right -= i-1

            if left == right:
                return i
            if left > right:
                break

        return -1
