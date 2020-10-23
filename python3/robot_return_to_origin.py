"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0

        n = len(moves)
        if n == 0:
            return True

        for i in moves:
            if i == "L":
                x -= 1
            elif i == "R":
                x += 1
            elif i == "U":
                y += 1
            elif i == "D":
                y -= 1

        print(x, y)

        if (x == 0) and (y == 0):
            return True

        return False
