from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        stack = []
        for num in nums:
            if num != 0:
                stack.append(num)

        return stack + [0 for _ in range(n - len(stack))]
