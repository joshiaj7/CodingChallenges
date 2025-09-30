from typing import List

"""
Space   : O(n)
Time    : O(n ** 2)
"""

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            n = len(nums)
            temp = []

            for i in range(n-1):
                num = (nums[i] + nums[i+1]) % 10
                temp.append(num)

            nums = temp    

        return nums[0]
        