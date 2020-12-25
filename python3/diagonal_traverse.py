class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        with direction check
        Space : O(m * n)
        Time  : O(m * n)
        """
        if not matrix:
            return []

        x, y = 0, 0
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        direction = "u"

        while y < row or x < col:
            ans.append(matrix[y][x])

            if y == row-1 and x == col-1:
                break

            if direction == "u":
                if y == 0 or x == col-1:
                    if x == col-1:
                        y += 1
                    else:
                        x += 1
                    direction = "d"
                else:
                    y -= 1
                    x += 1
            else:
                if x == 0 or y == row-1:
                    if y == row-1:
                        x += 1
                    else:
                        y += 1
                    direction = "u"
                else:
                    y += 1
                    x -= 1

        return ans

    def findDiagonalOrderNoDir(self, matrix: List[List[int]]) -> List[int]:
        """
        No direction check
        Space : O(m * n)
        Time  : O(m * n)
        """

        if not matrix:
            return matrix

        ans = []
        d = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i+j) not in d:
                    d[i+j] = [matrix[i][j]]
                else:
                    d[i+j].append(matrix[i][j])

        for k in range(len(d)):
            if k % 2 == 0:
                ans += d[k][::-1]
            else:
                ans += d[k]

        return ans
