"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = -10**10, -10**10, -10**10

        nums = list(set(nums))
        n = len(nums)

        for i in nums:
            a = max(i, a)

        if n <= 2:
            return a

        for j in nums:
            if j < a:
                b = max(b, j)

        for k in nums:
            if k < b:
                c = max(c, k)

        return c
