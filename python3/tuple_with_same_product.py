from typing import List
from collections import defaultdict

"""
Space   : O(n^2)
Time    : O(n^2)
"""

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        d = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                a = nums[i]
                b = nums[j]
                d[a * b] += 1
                
        for k, v in d.items():
            pairs = (v - 1) * v // 2
            ans += pairs * 8

        return ans

        