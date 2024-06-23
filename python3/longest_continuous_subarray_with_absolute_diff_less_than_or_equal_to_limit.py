from typing import List

"""
Space   : O(n)
Time    : O(n)
sliding window
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        n = len(nums)
        left = 0
        increase = []
        decrease = []
        
        for right in range(n):
            while increase and increase[-1] > nums[right]:
                increase.pop()
            increase.append(nums[right])

            while decrease and decrease[-1] < nums[right]:
                decrease.pop()
            decrease.append(nums[right])

            while decrease[0] - increase[0] > limit:
                if nums[left] == increase[0]:
                    increase.pop(0)
                if nums[left] == decrease[0]:
                    decrease.pop(0)
                left += 1

            ans = max(ans, right - left + 1)

        return ans
