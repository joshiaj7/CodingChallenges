"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 1:
            return

        point = 0
        found = False
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                found = True
                point = i
                break

        if not found:
            nums.sort()
        else:
            for j in range(n-1, -1, -1):
                if nums[j] > nums[point]:
                    nums[point], nums[j] = nums[j], nums[point]
                    break
            nums[point+1:] = nums[point+1:][::-1]
