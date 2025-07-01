from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        d = {}
        
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
                
        for k in d.keys():
            if k+1 in d:
                ans = max(ans, d[k] + d[k+1])
        
        return ans
