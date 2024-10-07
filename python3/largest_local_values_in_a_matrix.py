from typing import List

"""
Space   : O(n)
Time    : O(n^4)
"""

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(grid)
        
        for i in range(n-2):
            line = []
            for j in range(n-2):
                m = 0
                for u in range(3):
                    for v in range(3):
                        x = i + u
                        y = j + v
                        m = max(m, grid[x][y])    
                line.append(m)
            ans.append(line)
            
        return ans
