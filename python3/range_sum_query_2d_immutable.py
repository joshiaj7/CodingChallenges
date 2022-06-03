"""
Space   : O(mn)
Time    : O(mn)
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        row, col = len(matrix), len(matrix[0])
        for y in range(row):
            for x in range(1, col):
                self.matrix[y][x] += self.matrix[y][x-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for y in range(row1, row2+1):
            if col1 == 0:
                ans += self.matrix[y][col2]
            else:
                ans += self.matrix[y][col2] - self.matrix[y][col1-1]

        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
