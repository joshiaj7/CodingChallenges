"""
Space   : O(mn)
Time    : O(mn)
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m, self.n = len(heights), len(heights[0])
        p_visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        a_visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        coord = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(x, y, visited):
            if not visited[y][x]:
                visited[y][x] = True
                for dx, dy in coord:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < self.n and 0 <= ny < self.m and heights[ny][nx] >= heights[y][x]:
                        bfs(nx, ny, visited)

        # horizontal crawl
        for i in range(self.n):
            bfs(i, 0, p_visited)
            bfs(i, self.m-1, a_visited)

        # vertical crawl
        for j in range(self.m):
            bfs(0, j, p_visited)
            bfs(self.n-1, j, a_visited)

        # append if both true
        ans = []
        for j in range(self.m):
            for i in range(self.n):
                if p_visited[j][i] and a_visited[j][i]:
                    ans.append([j, i])

        return ans
