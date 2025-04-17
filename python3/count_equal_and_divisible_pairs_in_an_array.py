from collections import defaultdict
from typing import List

"""
Space   : O(n)  
Time    : O(n^2)
"""

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0

        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)

        for key, val in d.items():
            if len(val) <= 1:
                continue

            m = len(val)
            for i in range(m):
                for j in range(i+1, m):
                    if (val[i] * val[j]) % k == 0:
                        ans += 1

        return ans
        