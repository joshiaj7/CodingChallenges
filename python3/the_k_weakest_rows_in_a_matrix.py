from typing import List

"""
Space   : O(m)
Time    : O(mn + m log m)
"""


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        pairs = []

        for i in range(m):
            sol = 0
            j = 0
            while j < n:
                if mat[i][j] == 1:
                    sol += 1
                else:
                    break
                j += 1

            pairs.append((sol, i))
            
        pairs.sort(key=lambda x: (x[0], x[1]))
        
        return [x[1] for x in pairs[:k]]
