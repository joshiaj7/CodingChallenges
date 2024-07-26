from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []
        countMap = {}

        for i, v in enumerate(nums):
            if v in countMap:
                countMap[v] += 1
            else:
                countMap[v] = 1

        pairs = []
        for k, v in countMap.items():
            pairs.append((k, v))

        pairs.sort(key=lambda x: (x[1], -x[0]))
        for val, occ in pairs:
            ans += [val] * occ

        return ans
        