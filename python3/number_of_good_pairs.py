from collections import defaultdict
from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        hashmap = defaultdict(list)

        for i, v in enumerate(nums):
            hashmap[v].append(i)

        for k, v in hashmap.items():
            if len(v) > 1:
                for j in range(1, len(v)):
                    ans += j

        return ans

