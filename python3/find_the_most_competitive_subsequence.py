"""
Stack approach
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        i = 0

        n = len(nums)

        while i < n:
            while stack and nums[i] < stack[-1] and n-i+len(stack) > k:
                stack.pop()

            if len(stack) < k:
                stack.append(nums[i])

            i += 1

        return stack
