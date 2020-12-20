# Best solution
# Space : O(n**2)
# Time  : O(n**2)


class Solution:
    def cherryPickup(self, grid) -> int:
        nrow, ncol = len(grid), len(grid[0])

        # padding
        grid = [[0] + x + [0] for x in grid]

        # initialize dp
        dp = [[[0]*(ncol+2) for i in range(ncol+2)]]
        dp[0][1][ncol] = grid[0][1] + grid[0][ncol]

        for row in range(1, nrow):
            dp.append([[0]*(ncol+2) for i in range(ncol+2)])

            for r1 in range(1, min(row + 1, ncol) + 1):
                for r2 in range(max(1, ncol - row), ncol + 1):
                    if r1 == r2:
                        continue

                    dp[row][r1][r2] = max([
                        dp[row - 1][i][j] for i in [r1-1, r1, r1+1] for j in [r2-1, r2, r2+1]
                        if i != j]) + grid[row][r2] + grid[row][r1]

        return max(map(max, dp[-1]))
