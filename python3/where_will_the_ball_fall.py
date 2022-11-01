"""
Space   : O(n)
Time    : O(mn)
"""


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []

        for b in range(n):
            pos = b
            stuck = False

            for lvl in range(m):
                lean = grid[lvl][pos]

                # stuck to the wall
                if pos + lean < 0 or pos + lean >= n:
                    stuck = True
                    break

                # trapped in v shape
                if (lean == 1 and grid[lvl][pos+1] == -1) or (lean == -1 and grid[lvl][pos-1] == 1):
                    stuck = True
                    break

                pos += lean

            if stuck:
                ans.append(-1)
            else:
                ans.append(pos)

        return ans
