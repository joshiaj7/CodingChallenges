from typing import List

"""
Space   : O(mn)
Time    : O(mn)
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]

        neighbor = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    for di, dj in neighbor:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == 1:
                            queue.append((ni, nj))

        visited = set()
        level = 1
        while queue:
            temp = []
            for i, j in list(set(queue)):
                if (i, j) in visited:
                    continue
                
                ans[i][j] = level
                visited.add((i, j))
                for di, dj in neighbor:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == 1:
                        temp.append((ni, nj))

            level += 1
            queue = temp


        return ans
