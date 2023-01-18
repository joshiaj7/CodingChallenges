"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, max_sum, cur_max, min_sum, cur_min = 0, nums[0], 0, nums[0], 0

        for x in nums:
            total += x
            cur_max = max(cur_max + x, x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + x, x)
            min_sum = min(min_sum, cur_min)

        if max_sum > 0:
            return max(max_sum, total - min_sum)
        return max_sum
