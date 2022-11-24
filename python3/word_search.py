"""
Space   : O(mn)
Time    : O(mn * len(word))
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        nw = len(word)
        coord = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.res = False

        def dfs(x, y, i, path, visited):
            if path == word:
                self.res = True
                return

            for dx, dy in coord:
                nx = x + dx
                ny = y + dy
                if 0 <= ny < M and 0 <= nx < N and (nx, ny) not in visited:
                    if i < nw and board[ny][nx] == word[i + 1]:
                        dfs(nx, ny, i + 1, path + board[ny][nx], visited + [(x, y)])

        for y in range(M):
            for x in range(N):
                if board[y][x] == word[0]:
                    dfs(x, y, 0, board[y][x], [])
                    if self.res:
                        return True

        return False
