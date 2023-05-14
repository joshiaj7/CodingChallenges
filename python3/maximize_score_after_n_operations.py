from functools import lru_cache
from math import gcd

"""
Space   : O((2n) ^ n)
Time    : O(n * n!)
"""


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, mask: int) -> int:
            if i > len(nums) // 2:
                return 0

            res = 0
            for j in range(len(nums)):
                for k in range(j + 1, len(nums)):
                    new_mask = (1 << j) + (1 << k)
                    if not mask & new_mask:
                        res = max(res, i * gcd(nums[j], nums[k]) + dfs(i + 1, mask + new_mask))
            return res

        return dfs(1, 0)
