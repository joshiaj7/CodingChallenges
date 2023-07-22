"""
Space   : O(8^k)
Time    : O(8^k)
"""

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        memo = {}

        def dfs(x, y, prob, lvl):
            if 0 <= x < n and 0 <= y < n and lvl < k:
                sum_prob = 0
                for dx, dy in moves:
                    nx = x + dx
                    ny = y + dy
                    if (nx, ny, lvl) not in memo:
                        memo[(nx, ny, lvl)] = dfs(nx, ny, prob/8, lvl + 1)
                    sum_prob += memo[(nx, ny, lvl)]
                return sum_prob
            else:
                if 0 <= x < n and 0 <= y < n:
                    return prob
                else:
                    return 0

        return dfs(column, row, 1, 0)
