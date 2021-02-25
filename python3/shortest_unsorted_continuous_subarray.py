"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = n-1, 0

        isAsc = True
        forward = nums[0]
        for i in range(1, n):
            if nums[i] < forward:
                end = max(end, i)
                isAsc = False
            forward = max(forward, nums[i])

        if isAsc:
            return 0

        backward = nums[-1]
        for j in range(n-2, -1, -1):
            if nums[j] > backward:
                start = min(start, j)
            backward = min(backward, nums[j])

        return end - start + 1
