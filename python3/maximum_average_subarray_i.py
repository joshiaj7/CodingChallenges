"""
Space   : O(1)
Time    : O(n)
Sliding Window method
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        ans = float('-inf')

        start = 0
        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            if i >= k-1:
                ans = max(ans, cur_sum/k)
                cur_sum -= nums[start]
                start += 1

        return ans
