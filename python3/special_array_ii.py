from typing import List

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        n = len(nums)
        prefix = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1]
            prev = nums[i-1] % 2
            curr = nums[i] % 2

            if prev == curr:
                prefix[i] += 1

        for s, e in queries:
            special = prefix[e] - (prefix[s] if s > 0 else 0)
            ans.append(special == 0)

        return ans
        