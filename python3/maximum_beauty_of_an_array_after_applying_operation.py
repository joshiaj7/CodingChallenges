from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        nums.sort()

        if n == 1:
            return 1

        i, j = 0, 0
        while j < n:
            while i < n and nums[j] - nums[i] > 2 * k:
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans
        