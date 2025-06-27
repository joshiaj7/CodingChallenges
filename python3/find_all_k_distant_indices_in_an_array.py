from collections import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        n = len(nums)

        keyIdx = []
        for i in range(n):
            if nums[i] == key:
                keyIdx.append(i)

        m = len(keyIdx)
        if m == 0:
            return []

        j = 0
        for i in range(n):
   
            # first check
            if abs(keyIdx[j] - i) <= k:
                ans.append(i)
            # second check
            elif keyIdx[j] - i < 0 and j+1 < m:
                j += 1
                
                if abs(keyIdx[j] - i) <= k:
                    ans.append(i)
                

        return ans
        