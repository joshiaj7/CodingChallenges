"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = -10**10, -10**10, -10**10

        nums = list(set(nums))

        for i in nums:
            if i > a:
                c = b
                b = a
                a = i
            elif i > b:
                c = b
                b = i
            elif i > c:
                c = i

        if c == -10**10:
            return a
        return c
