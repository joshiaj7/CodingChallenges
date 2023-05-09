"""
Space   : O(mn)
Time    : O(mn)
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        direction = "r"
        i, j = 0, 0
        visited = set()

        def generate_coord(i, j, direction):
            if direction == "r":
                return i, j + 1
            elif direction == "l":
                return i, j - 1
            elif direction == "u":
                return i - 1, j
            return i + 1, j

        while True:
            ans.append(matrix[i][j])
            visited.add((i, j))
            if len(ans)  == m * n:
                break

            ni, nj = generate_coord(i, j, direction)
            if (ni, nj) in visited or (ni < 0 or ni >= m or nj < 0 or nj >= n):
                if direction == "r":
                    direction = "d"
                elif direction == "d":
                    direction = "l"
                elif direction == "l":
                    direction = "u"
                else:
                    direction = "r"
                
            i, j = generate_coord(i, j, direction)
 


        return ans
