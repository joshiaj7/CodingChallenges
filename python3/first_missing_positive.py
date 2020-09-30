"""
space   : O(1)
time    : O(n)
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hasOne = False
        n = len(nums)

        for idx in range(n):
            if nums[idx] < 0:
                nums[idx] = 0
            elif nums[idx] == 1:
                hasOne = True

        if not hasOne:
            return 1

        for i in range(n):
            currNum = abs(nums[i])
            if currNum > 0 and currNum <= n:
                if nums[currNum - 1] == 0:
                    nums[currNum - 1] = -1
                elif nums[currNum - 1] > 0:
                    nums[currNum - 1] *= -1

        for j in range(n):
            if nums[j] > -1:
                return j + 1

        return n + 1
