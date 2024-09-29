from typing import List

"""
Space   : O(n)
Time    : O(nm)
"""

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        h1 = {}

        for x in set(arr1):
            for i in range(len(str(x))):
                pref = str(x)[:i+1]
                h1[pref] = 1

        for x in set(arr2):
            for i in range(len(str(x))):
                pref = str(x)[:i+1]
                if pref in h1:
                    ans = max(ans, len(pref))
                else:
                    break

        return ans
        