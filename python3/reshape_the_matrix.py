# Space : O(1)
# Time  : O(r*c)

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        if row*col != r*c:
            return mat

        ans = [[] for _ in range(r)]
        point = 0
        for y in range(row):
            for x in range(col):
                ans[point].append(mat[y][x])
                if len(ans[point]) == c:
                    point += 1

        return ans
