"""
Space   : O(m*n)
Time    : O(m*n)
"""


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        temp = []

        k %= row * col

        for x in grid:
            temp.extend(x)

        temp = temp[-k:] + temp[:-k]

        p = 0
        for y in range(row):
            for x in range(col):
                grid[y][x] = temp[p]
                p += 1

        return grid
