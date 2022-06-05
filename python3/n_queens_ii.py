"""
Space   : O(n)
Time    : O(n**2)

method:
dfs
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, c, diffs, sums):
            nonlocal ans
            q = len(queens)
            if q == n:
                ans += 1
                return
            if q == 0:
                for i in range(n):
                    dfs(queens + [i], c[:i] + c[i+1:],
                        diffs + [q - i], sums + [q + i])
            else:
                for i, v in enumerate(c):
                    if q-v in diffs or q+v in sums:
                        continue
                    dfs(queens + [v], c[:i] + c[i+1:],
                        diffs + [q-v], sums + [q+v])

        ans = 0
        cols = [i for i in range(n)]
        dfs([], cols, [], [])
        return ans
