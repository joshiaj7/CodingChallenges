from typing import List

"""
Space   : O(nm)
Time    : O(4nm)
"""


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ans = 0
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for row, col in walls:
            grid[row][col] = 1
        for row, col in guards:
            grid[row][col] = 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for y, x in guards:
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                while 0 <= ny < m and 0 <= nx < n:
                    if grid[ny][nx] == 1:
                        break
                    if grid[ny][nx] == 0:
                        grid[ny][nx] = 2
                    ny += dy
                    nx += dx

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 0:
                    ans += 1
    
        return ans
