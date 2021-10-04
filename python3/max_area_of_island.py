# Space     : O(n)
# Time      : O(m*n)
class Solution:
    def crawl(self, grid, x, y):
        def bfs(dx, dy):
            nonlocal area
            if grid[dy][dx] == 1:
                area += 1
                grid[dy][dx] = 0
            elif grid[dy][dx] == 0:
                return

            for ax, ay in c:
                if 0 <= dy + ay < row and 0 <= dx + ax < col:
                    if grid[dy+ay][dx+ax] == 1:
                        bfs(dx+ax, dy+ay)

        row = len(grid)
        col = len(grid[0])
        c = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        area = 0
        bfs(x, y)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0

        for y in range(row):
            for x in range(col):
                if grid[y][x] == 1:
                    ans = max(ans, self.crawl(grid, x, y))

        return ans
