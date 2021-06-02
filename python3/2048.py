import random


def validateTarget(T):
    if T == 1:
        return False

    b = bin(T)[2:]

    ones = 0
    for bit in b:
        if bit == '1':
            ones += 1

    if ones != 1:
        return False

    return True


def getEmptySpace(board, N):
    empty_coords = []
    for y in range(N):
        for x in range(N):
            if not board[y][x]:
                empty_coords.append((x, y))

    return empty_coords


def spawnNumber(board, empty_coords, init):
    rep = 2 if init else 1
    rep = rep if len(empty_coords) > 1 else 1

    for i in range(rep):
        rand_coord = random.randint(0, len(empty_coords)-1)
        x, y = empty_coords[rand_coord]
        if random.randint(0, 9) == 0:
            board[y][x] = 4
        else:
            board[y][x] = 2
        empty_coords = empty_coords[:rand_coord] + empty_coords[rand_coord+1:]


def createBoard(N):
    board = []
    for i in range(N):
        board.append([None for j in range(N)])

    return board


def printBoard(board):
    N = len(board)

    for y in range(N*2+1):
        if y % 2 == 0:
            line = "="
            for x in range(N):
                line += "====="
        else:
            line = "|"
            for x in range(N):
                if not board[y//2][x]:
                    line += "    |"
                elif board[y//2][x] >= 1000:
                    line += "{}|".format(board[y//2][x])
                elif board[y//2][x] >= 100:
                    line += "{} |".format(board[y//2][x])
                elif board[y//2][x] >= 10:
                    line += " {} |".format(board[y//2][x])
                elif board[y//2][x] >= 0:
                    line += " {}  |".format(board[y//2][x])
        print(line)


def sortLine(line, N):
    for i in range(N):
        for j in range(i+1, N):
            if not line[i]:
                line[i] = line[j]
                line[j] = None
            elif line[i] == line[j] and line[i]:
                line[i] += line[j]
                line[j] = None
                break
            elif line[i] and line[j] and line[i] != line[j]:
                break


def tiltUp(board):
    N = len(board)
    is_tilted = False

    for x in range(N):
        line = []

        # get per line
        for y in range(N):
            line.append(board[y][x])

        prev_line = line.copy()

        # bubble sort
        sortLine(line, N)

        if prev_line != line:
            is_tilted = True

        for y in range(N):
            board[y][x] = line[y]

    return is_tilted


def tiltLeft(board):
    N = len(board)
    is_tilted = False

    for y in range(N):
        line = []

        # get per line
        for x in range(N):
            line.append(board[y][x])

        prev_line = line.copy()

        # bubble sort
        sortLine(line, N)

        if prev_line != line:
            is_tilted = True

        for x in range(N):
            board[y][x] = line[x]

    return is_tilted


def tiltDown(board):
    N = len(board)
    is_tilted = False

    for x in range(N):
        line = []

        # get per line
        for y in range(N-1, -1, -1):
            line.append(board[y][x])

        prev_line = line.copy()

        # bubble sort
        sortLine(line, N)

        if prev_line != line:
            is_tilted = True

        for y in range(N-1, -1, -1):
            board[y][x] = line[N-1-y]

    return is_tilted


def tiltRight(board):
    N = len(board)
    is_tilted = False

    for y in range(N):
        line = []

        # get per line
        for x in range(N-1, -1, -1):
            line.append(board[y][x])

        prev_line = line.copy()

        # bubble sort
        sortLine(line, N)

        if prev_line != line:
            is_tilted = True

        for x in range(N-1, -1, -1):
            board[y][x] = line[N-1-x]

    return is_tilted


def moveBoard(board, d):
    if d == "w":
        is_tilted = tiltUp(board)
    elif d == "a":
        is_tilted = tiltLeft(board)
    elif d == "s":
        is_tilted = tiltDown(board)
    elif d == "d":
        is_tilted = tiltRight(board)

    return is_tilted


def checkIfWin(board, T):
    # 1. No deadlock
    # 2. Empty space available

    N = len(board)

    for y in range(N):
        for x in range(N):
            # check win
            if board[y][x] == T:
                return "win"

    return "continue"


def checkIfDeadlock(board):
    N = len(board)
    c = [(1, 0), (0, 1)]

    # check deadlock
    is_deadlock = True
    for y in range(N):
        for x in range(N):
            for ax, ay in c:
                if 0 <= x + ax < N and 0 <= y + ay < N:
                    if board[y][x] == board[y+ay][x+ax]:
                        is_deadlock = False

    if is_deadlock:
        return "lose"

    return "continue"


def playGame():
    print("Input board size: ")
    N = int(input())
    if N <= 0:
        print("Board size has to be >= 1")
        return

    print("Input target: ")
    T = int(input())
    is_valid = validateTarget(T)
    if not is_valid:
        print("Target must be power of 2 and >= 2")
        return

    if N == 1 and T != 2:
        print("Target is impossible")
        return

    # initial
    board = createBoard(N)
    empty_coords = getEmptySpace(board, N)
    spawnNumber(board, empty_coords, True)

    if N == 1 and T == 2:
        print("==========================")
        print("CONGRATULATIONS! YOU WON!")
        print("==========================")
        printBoard(board)
        return

    # play game
    result = ""
    while True:
        printBoard(board)

        # direction accepts WASD
        print("Enter direction (wasd) : ")
        d = input().lower()

        is_tilted = moveBoard(board, d)
        result = checkIfWin(board, T)
        if result == "win":
            break

        # spawn another number
        if is_tilted:
            empty_coords = getEmptySpace(board, N)
            spawnNumber(board, empty_coords, False)
            if len(empty_coords) == 0:
                result = checkIfDeadlock(board)
                if result == "lose":
                    break
        else:
            print("untilted")

    if result == "win":
        print("==========================")
        print("CONGRATULATIONS! YOU WON!")
        print("==========================")
    if result == "lose":
        print("===================")
        print("TOO BAD! YOU LOSE!")
        print("===================")
    printBoard(board)


if __name__ == "__main__":
    playGame()
