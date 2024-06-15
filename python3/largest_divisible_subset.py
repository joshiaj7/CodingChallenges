from typing import List

"""
Space   : O(n)
Time    : O(n^2)
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        ans = [[num] for num in nums]
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(ans[i]) < len(ans[j]) + 1 :
                    ans[i] = ans[j] + [nums[i]]

        maxSubset = max(ans, key=len)

        return maxSubset
