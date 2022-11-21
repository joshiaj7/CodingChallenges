"""
Space   : O(mn)
Time    : O(mn)
"""


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        visited = set()

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        sy, sx = entrance

        def is_exit(x, y, N, M):
            if x * y == 0 or x == N - 1 or y == M - 1:
                return True
            return False

        stack = [(sx, sy, 0)]
        while stack:
            temp = set()

            for x, y, val in stack:
                visited.add((x, y))
                if is_exit(x, y, N, M):
                    if val > 0:
                        return val

                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if (
                        0 <= nx < N
                        and 0 <= ny < M
                        and maze[ny][nx] == "."
                        and (nx, ny) not in visited
                    ):
                        temp.add((nx, ny, val + 1))

            stack = list(temp)

        return -1
