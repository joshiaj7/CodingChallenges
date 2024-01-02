from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        h = {}

        for x in nums:
            if x in h:
                h[x] += 1
            else:
                h[x] = 1
        
        while True:
            all_zero = True
            row = []

            for k, v in h.items():
                if v > 0:
                    all_zero = False
                    row.append(k)
                    h[k] -= 1
            
            if all_zero:
                break

            ans.append(row)
            
        return ans
        