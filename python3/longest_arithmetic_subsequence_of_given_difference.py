from typing import List

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap = dict()
        ans = 0

        for x in arr:
            if x - difference not in hashmap:
                hashmap[x] = 0
            else:
                hashmap[x] = hashmap[x-difference] + 1
                ans = max(ans, hashmap[x])

        return ans + 1
