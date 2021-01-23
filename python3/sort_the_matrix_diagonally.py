"""
Space   : O(nm)
Time    : O(nm)
"""


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        d = {}

        for y in range(row):
            for x in range(col):
                if y-x not in d:
                    d[y-x] = [mat[y][x]]
                else:
                    d[y-x].append(mat[y][x])

        for k in d.keys():
            d[k] = sorted(d[k])

        for y in range(row):
            for x in range(col):
                mat[y][x] = d[y-x].pop(0)

        return mat
