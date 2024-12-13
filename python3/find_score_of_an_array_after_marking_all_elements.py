from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        pairs = []
        mem = [0] * n

        for i, v in enumerate(nums):
            pairs.append((v, i))

        pairs.sort(key=lambda x: (x[0], x[1]))

        for val, idx in pairs:
            if mem[idx] == 1:
                continue

            ans += val
            mem[idx] = 1

            if idx > 0:
                mem[idx-1] = 1
            
            if idx < n-1:
                mem[idx+1] = 1

        return ans
        