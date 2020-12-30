class Solution:
    def getNeighbor(self, board: List[List[int]], x: int, y: int) -> int:
        neighbor = 0

        # left
        if x > 0 and board[y][x-1] == 1:
            neighbor += 1

        # right
        if x < len(board[0])-1 and board[y][x+1] == 1:
            neighbor += 1

        # up
        if y > 0 and board[y-1][x] == 1:
            neighbor += 1

        # down
        if y < len(board)-1 and board[y+1][x] == 1:
            neighbor += 1

        # left-up
        if x > 0 and y > 0 and board[y-1][x-1] == 1:
            neighbor += 1

        # left-down
        if x > 0 and y < len(board)-1 and board[y+1][x-1] == 1:
            neighbor += 1

        # right-up
        if x < len(board[0])-1 and y > 0 and board[y-1][x+1] == 1:
            neighbor += 1

        # right-down
        if x < len(board[0])-1 and y < len(board)-1 and board[y+1][x+1] == 1:
            neighbor += 1

        return neighbor

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        mem = [[0] * col for _ in range(row)]

        for y in range(row):
            for x in range(col):
                neighbor = self.getNeighbor(board, x, y)
                if board[y][x] == 1:
                    if neighbor >= 2 and neighbor <= 3:
                        mem[y][x] = 1
                    else:
                        mem[y][x] = 0
                else:
                    if neighbor == 3:
                        mem[y][x] = 1

        for i in range(row):
            for j in range(col):
                board[i][j] = mem[i][j]
