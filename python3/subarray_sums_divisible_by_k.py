"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans, prefix = 0, 0
        count = [1] + [0] * k

        for x in nums:
            prefix = (prefix + x) % k
            ans += count[prefix]
            count[prefix] += 1

        return ans
