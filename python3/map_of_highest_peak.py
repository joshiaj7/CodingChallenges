class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        ans = [[-1 for _ in range(m)] for _ in range(n)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # fill water
        stack = []
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    stack.append((i, j))

        level = 0
        while stack:
            temp = []
            for i, j in stack:
                if ans[i][j] != -1:
                    continue

                ans[i][j] = level
                for di, dj in directions:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < m and ans[ni][nj] == -1:
                        temp.append((ni, nj))

            stack = temp
            level += 1

        return ans
        