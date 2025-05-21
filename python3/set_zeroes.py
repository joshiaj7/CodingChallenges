from typing import List

"""
Space   : O(n + m)
Time    : O(nm)
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        colmap = {}
        rowmap = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowmap[i] = 1
                    colmap[j] = 1

        for i in rowmap.keys():
            for j in range(n):
                matrix[i][j] = 0

        for i in range(m):
            for j in colmap.keys():
                matrix[i][j] = 0


        