"""
Space   : O(n)
Time    : O(n)

Method:
Stack

32 is already ordered, only reversed
only need to find the 1
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        n2 = -float('inf')
        stack = []

        for i in range(n-1, -1, -1):
            if nums[i] < n2:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    n2 = stack.pop()
            stack.append(nums[i])

        return False
