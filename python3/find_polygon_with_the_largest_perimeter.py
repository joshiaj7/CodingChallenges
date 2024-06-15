from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        
        ans = -1
        nums.sort()
        sumArr = [0] * n

        for i, num in enumerate(nums):
            if i == 0:
                sumArr[i] = num
                continue
            
            sumArr[i] = sumArr[i-1] + num
            if i >= 2 and num < sumArr[i-1]:
                ans = sumArr[i] 

        return ans