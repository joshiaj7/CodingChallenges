import random


def spawnBombs(mines, row, col):
    mines_coords = set()
    while mines > 0:
        y = random.randint(0, row-1)
        x = random.randint(0, col-1)

        if (x, y) not in mines_coords:
            mines_coords.add((x, y))
            mines -= 1

    return mines_coords


def createBoard(row, col):
    board = []
    for i in range(row):
        board.append(['O' for j in range(col)])

    return board


def calculateBoard(row, col, mine_coords):
    board = createBoard(row, col)
    c = [(0, -1), (0, 1), (-1, 0), (1, 0),
         (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for y in range(row):
        for x in range(col):
            if (x, y) in mine_coords:
                board[y][x] = 'X'
                for ax, ay in c:
                    if (0 <= x + ax < col) and (0 <= y + ay < row) and (x + ax, y + ay) not in mine_coords:
                        if board[y+ay][x+ax] == 'O':
                            board[y+ay][x+ax] = '1'
                        elif board[y+ay][x+ax].isdigit():
                            board[y+ay][x +
                                        ax] = str(int(board[y+ay][x+ax])+1)

    return board


def printBoard(board):
    rows = len(board)
    cols = len(board[0])

    for y in range(rows+2):
        if y == 0:
            line = "    "
            for x in range(cols):
                line += "{} ".format(x)
        elif y == 1:
            line = "    "
            for x in range(cols):
                line += "= "
        else:
            line = "{} | ".format(y-2)
            for x in range(cols):
                line += "{} ".format(board[y-2][x])
        print(line)


def openBoard(board, ans_board, x, y):
    def dfs(dx, dy):
        if board[dy][dx] == 'O':
            if ans_board[dy][dx].isdigit():
                board[dy][dx] = ans_board[dy][dx]
                return board

            board[dy][dx] = '_'
            for ax, ay in c:
                if (0 <= dx + ax < col) and (0 <= dy + ay < row):
                    dfs(dx + ax, dy + ay)

    c = [(0, -1), (0, 1), (-1, 0), (1, 0),
         (-1, -1), (-1, 1), (1, -1), (1, 1)]
    row = len(board)
    col = len(board[0])
    dfs(x, y)

    return board


def checkIsWin(board, mine_coords):
    row = len(board)
    col = len(board[0])

    for y in range(row):
        for x in range(col):
            if board[y][x] == 'O' and (x, y) not in mine_coords:
                return False

    return True


def checkBoard(board, ans_board, mine_coords, x, y):
    # hit mine
    if (x, y) in mine_coords:
        for bx, by in mine_coords:
            board[by][bx] = 'X'
        return board, "lose"

    # already inputted validation
    if board[y][x].isdigit() or board[y][x] == " ":
        print("coordinate {} {} has already inputted")
        print("please choose another coordinate")
        return board, "continue"

    # check for new hit
    board = openBoard(board, ans_board, x, y)

    # check if there's still coord to choose
    # otherwise, player wins
    isWin = checkIsWin(board, mine_coords)

    if isWin:
        return board, "win"

    return board, "continue"


def playGame():
    mines = 5
    row = 5
    col = 10
    board = createBoard(row, col)
    mine_coords = spawnBombs(mines, row, col)
    ans_board = calculateBoard(row, col, mine_coords)

    print(mine_coords)
    printBoard(ans_board)

    result = "continue"
    while result == "continue":
        printBoard(board)
        print("Input coordinate (x y). example: 0 1")
        user_input = input()
        x, y = user_input.split(" ")

        board, result = checkBoard(
            board, ans_board, mine_coords, int(x), int(y))

    if result == "win" or result == "lose":
        printBoard(board)
        return result

    return result


if __name__ == "__main__":
    print("===== MINESWEEPER =====")
    print("1. Play game")
    print("2. Quit")
    print("Enter number: ")
    action = input()

    if action == '1':
        result = playGame()
        if result == "win":
            print("CONRATULATIONS, YOU WIN!")
        elif result == "lose":
            print("YOU LOSE!")
