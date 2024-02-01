from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        temp = []
        for x in nums:
            if not temp:
                temp.append(x)
                continue
            else:
                if x - temp[0] <= k:
                    temp.append(x)
                else:
                    return [] 

            if len(temp) == 3:
                ans.append(temp)
                temp = []
            

        return ans
