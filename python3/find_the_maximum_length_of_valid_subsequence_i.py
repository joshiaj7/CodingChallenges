from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        parity = []
        for i in range(n):
            parity.append(nums[i]  % 2)

        onlyOnes = 0
        onlyZeroes = 0
        curr = parity[0]
        longestCurr = 1
        for i, p in enumerate(parity):
            if p == 0:
                onlyZeroes += 1
            else:
                onlyOnes += 1

            if i > 0 and curr != p:
                curr = p
                longestCurr += 1    

        return max(onlyZeroes, onlyOnes, longestCurr)

        