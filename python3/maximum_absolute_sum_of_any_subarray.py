from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0

        # check positive
        total = 0
        for num in nums:
            total += num
            if total < 0:
                total = 0

            ans = max(ans, total)

        # check negative
        total = 0
        for num in nums:
            total += num
            if total > 0:
                total = 0

            ans = max(ans, abs(total))

        return ans
        