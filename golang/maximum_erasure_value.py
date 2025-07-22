from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        i = 0
        count = 0
        d = {}
        for j, num in enumerate(nums):
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
            count += num
            
            while i < j and d[num] > 1:
                omitNum = nums[i]
                count -= omitNum
                d[omitNum] -= 1
                i += 1
                
            ans = max(ans, count)

        return ans
        