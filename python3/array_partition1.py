"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        leng = len(nums)

        nums = sorted(nums)

        for idx in range(0, leng, 2):
            ans += min(nums[idx], nums[idx+1])

        return ans
