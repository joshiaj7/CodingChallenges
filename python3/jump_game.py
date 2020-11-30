"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        cred = 0
        i = 0
        while True:
            cred = max(cred, nums[i])
            if cred + i >= n-1:
                return True
            if cred == 0:
                break

            i += 1
            cred -= 1

        return False
