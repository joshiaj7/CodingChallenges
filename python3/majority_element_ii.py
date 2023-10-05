from typing import List

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        hashmap = {}
        
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        
        for k, v in hashmap.items():
            if v > (n / 3):
                ans.append(k)

        return ans
