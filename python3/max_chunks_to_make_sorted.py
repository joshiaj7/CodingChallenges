from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        val_sum, idx_sum = 0, 0
        for i, v in enumerate(arr):
            val_sum += v
            idx_sum += i
            if val_sum == idx_sum:
                ans += 1

        return ans
        