"""
Space   : O(m * n)
Time    : O(m * n)
"""


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        row = len(mat)
        col = len(mat[0])
        d = {}

        idx = 0
        for x in range(col):
            for y in range(row):
                if y not in d and mat[y][x] == 0:
                    d[y] = idx
                    idx += 1

        if len(d) < k:
            for i in range(row):
                if i not in d:
                    d[i] = idx
                    idx += 1

        for k, v in d.items():
            if v < len(ans):
                ans[v] = k

        return ans
