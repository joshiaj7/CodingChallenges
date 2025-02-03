from typing import List

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        direction = "."
        n = len(nums)

        curr = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                if direction != "+":
                    curr = 2
                    direction = "+"
                else:
                    curr += 1
            elif nums[i] < nums[i-1]:
                if direction != "-":
                    curr = 2
                    direction = "-"
                else:
                    curr += 1
            else:
                direction = "."
                curr = 1

            ans = max(ans, curr)

        return ans
        