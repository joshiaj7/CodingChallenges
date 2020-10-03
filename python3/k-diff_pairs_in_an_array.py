"""
space   : O(n)
time    : O(n)
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        ans = 0
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        for key in hashmap.keys():
            if k != 0:
                if key + k in hashmap:
                    ans += 1
            else:
                if hashmap[key] > 1:
                    ans += 1

        return ans
