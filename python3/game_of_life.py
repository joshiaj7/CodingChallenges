"""
Space   : O(m*n)
Time    : O(m*n)
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # live
        # n < 2  -> 0
        # n == 2 / 3 -> 1
        # n > 3 -> 0

        # dead
        # n == 3 -> 1

        row = len(board)
        col = len(board[0])
        neighbors = []
        coord = [(0, 1), (1, 0), (0, -1), (-1, 0),
                 (1, 1), (-1, -1), (1, -1), (-1, 1)]

        # fill neighbors
        for r in range(row):
            line = []
            for c in range(col):
                live = 0
                for x, y in coord:
                    if (r+y) >= 0 and (r+y) < row and (c+x) >= 0 and c+x < col:
                        if board[r+y][c+x] == 1:
                            live += 1
                line.append(live)
            neighbors.append(line)

        for r in range(row):
            for c in range(col):
                i = 0
                if board[r][c] == 1:
                    if neighbors[r][c] < 2 or neighbors[r][c] > 3:
                        i = 0
                    else:
                        i = 1
                else:
                    if neighbors[r][c] == 3:
                        i = 1
                board[r][c] = i
