from collections import defaultdict

"""
Space   : O(1)
Time    : O(1)
space and time in constant time because board size is constant
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def boxHelper(x, y, box_num):
            if board[y][x] in box_map[box_num]:
                return False

            box_map[box_num].add(board[y][x])
            return True

        row_map = defaultdict(set)
        col_map = defaultdict(set)
        box_map = defaultdict(set)

        for y in range(9):
            for x in range(9):
                if board[y][x] != ".":
                    # insert row
                    if board[y][x] in row_map[y]:
                        return False
                    else:
                        row_map[y].add(board[y][x])

                    # insert col
                    if board[y][x] in col_map[x]:
                        return False
                    else:
                        col_map[x].add(board[y][x])

                    box_res = True
                    # box 1
                    if y < 3:
                        if x < 3:
                            box_res = boxHelper(x, y, 1)
                        elif x < 6:
                            box_res = boxHelper(x, y, 2)
                        else:
                            box_res = boxHelper(x, y, 3)
                    elif y < 6:
                        if x < 3:
                            box_res = boxHelper(x, y, 4)
                        elif x < 6:
                            box_res = boxHelper(x, y, 5)
                        else:
                            box_res = boxHelper(x, y, 6)
                    else:
                        if x < 3:
                            box_res = boxHelper(x, y, 7)
                        elif x < 6:
                            box_res = boxHelper(x, y, 8)
                        else:
                            box_res = boxHelper(x, y, 9)

                    if not box_res:
                        return False

        return True
