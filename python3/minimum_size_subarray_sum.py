from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        i = 0

        for j in range(n):
            target -= nums[j]
            while target <= 0:
                ans = min(ans, j - i + 1)
                target += nums[i]
                i += 1

        return ans % (n + 1)
