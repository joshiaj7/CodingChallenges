from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1

        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1


        for k, v in d.items():
            if k == v:
                ans = max(ans, k)

        return ans
        