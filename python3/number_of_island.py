"""
Space   : O(n)
Time    : O(mn)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def crawl(x, y):
            if grid[y][x] == "1":
                grid[y][x] = "0"
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < self.n and 0 <= ny < self.m:
                        crawl(nx, ny)

        self.m, self.n = len(grid), len(grid[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0

        for y in range(self.m):
            for x in range(self.n):
                if grid[y][x] == "1":
                    crawl(x, y)
                    ans += 1

        return ans
