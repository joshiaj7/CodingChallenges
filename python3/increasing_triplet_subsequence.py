"""
Space : O(1)
Time  : O(n)
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 3:
            return False

        a = 2**32 - 1
        b = 2**32 - 1

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True

        return False
