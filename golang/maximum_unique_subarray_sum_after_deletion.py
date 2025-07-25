from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0

        maxNum = max(nums)
        if maxNum < 0:
            return maxNum

        s = set()
        for num in nums:
            if num <= 0 or num in s:
                continue

            s.add(num)
            ans += num

        return ans
        