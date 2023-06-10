"""
Space   : O(1)
Time    : O(log(maxSum))
"""

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(mid):
            # sum of arithmetic sequence (nums) first half 
            # increasing
            i = max(mid - index, 0)
            res = (mid + i) * (mid - i + 1) // 2

            # sum of arithmetic sequence (nums) second half
            # decreasing
            i = max(mid - ((n-1) - index), 0)
            res += (mid + i) * (mid - i + 1) // 2
            return res - mid

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left + 1
