# Space : O(n**2)
# Time  : O(n**2)

class Solution:
    def updateCoor(self, x, y, direction):
        if direction == 'x+':
            return x + 1, y
        elif direction == 'x-':
            return x - 1, y
        elif direction == 'y+':
            return x, y + 1
        else:
            return x, y - 1

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            matrix.append([0]*n)

        i = 1
        x, y = 0, 0
        direction = "x+"
        while i <= n*n:
            matrix[y][x] = i
            if direction == "x+":
                if x == n-1 or matrix[y][x+1] > 0:
                    direction = "y+"

            if direction == "x-":
                if x == 0 or matrix[y][x-1] > 0:
                    direction = "y-"

            if direction == "y+":
                if y == n-1 or matrix[y+1][x] > 0:
                    direction = "x-"

            if direction == "y-":
                if y == 0 or matrix[y-1][x] > 0:
                    direction = "x+"

            i += 1
            x, y = self.updateCoor(x, y, direction)
        return matrix
