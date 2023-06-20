from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        size = (2 * k) + 1

        ans = [-1] * n
        if n < size:
            return ans

        i = k
        total = 0
        for j, val in enumerate(nums):
            total += val
            if j - size >= 0:
                total -= nums[j-size]

            if j >= size - 1:
                ans[i] = total // size
                i += 1

        return ans
