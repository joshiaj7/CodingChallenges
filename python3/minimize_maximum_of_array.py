"""
Space   : O(1)
Time    : O(n)

Method:
Prefix average
"""


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0

        count = 0
        for i, x in enumerate(nums):
            count += x
            ans = max(ans, (count + i) // (i + 1))

        return ans
