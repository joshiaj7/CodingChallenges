from collections import defaultdict

"""
Space   : O(nm)
Time    : O(nm log n)
"""


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = defaultdict(list)

        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])

        for k, _ in d.items():
            d[k].sort()

        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop(0)

        return mat
