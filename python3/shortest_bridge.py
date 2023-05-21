from collections import defaultdict
from typing import List 

"""
Space   : O(n^2)
Time    : O(n^2)
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ans = 100000
        n = len(grid)
        coords = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        outer = defaultdict(set)
        visited = [[-1 for _ in range(n)] for _ in range(n)]

        def dfs(i, j, sign):
            if grid[i][j] == 1 and visited[i][j] == -1:
                visited[i][j] = 1
                for di, dj in coords:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 0:
                            outer[sign].add((i, j))
                        elif visited[ni][nj] == -1:
                            dfs(ni, nj, sign)

        for i in range(n):
            for j in range(n):
                if len(outer[1]) == 0:
                    dfs(i, j, 1)
                else:
                    dfs(i, j, 2)

        for x1, y1 in outer[1]:
            for x2, y2 in outer[2]:
                ans = min(ans, abs(x1 - x2) + abs(y1 - y2) - 1)

        return ans
