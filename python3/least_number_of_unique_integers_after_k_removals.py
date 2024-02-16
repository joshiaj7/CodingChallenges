from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ans = 0
        hashmap = {}

        for x in arr:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1

        n = len(hashmap)
        ans = n
        val_list = list(hashmap.values())
        val_list.sort()

        for x in val_list:
            if x <= k:
                k -= x
                ans -= 1
            else:
                break

        return ans
