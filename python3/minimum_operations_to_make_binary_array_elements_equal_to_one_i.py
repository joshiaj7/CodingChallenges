from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def notBit(i):
            if i == 0:
                return 1
            return 0

        for i in range(n):
            if nums[i] == 0:
                if n - i >= 3:
                    nums[i] = notBit(nums[i])
                    nums[i+1] = notBit(nums[i+1])
                    nums[i+2] = notBit(nums[i+2])
                    ans += 1
                else:
                    return -1

        return ans
        