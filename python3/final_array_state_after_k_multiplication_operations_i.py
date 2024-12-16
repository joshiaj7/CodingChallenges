from typing import List

"""
Space   : O(1)
Tiem    : O(nk)
"""


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            mi = float('inf')
            idx = 0

            for i, x in enumerate(nums):
                if x < mi:
                    mi = min(mi, x)
                    idx = i

            nums[idx] *= multiplier

        return nums
        