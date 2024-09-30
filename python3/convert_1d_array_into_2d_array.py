from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original) 
        
        if l != m*n:
            return []
        
        ans = []
        temp = []
        for i in range(l):
            temp.append(original[i])

            if len(temp) == n:
                ans.append(temp)
                temp = []

        return ans
        