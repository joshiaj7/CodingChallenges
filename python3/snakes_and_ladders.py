"""
Space   : O(n^2)
Time    : O(n^2)
"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        need = {1: 0}
        n = len(board)
        stack = [1]

        while stack:
            x = stack.pop(0)
            for i in range(x + 1, x + 7):
                a, b = (i - 1) // n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0:
                    i = nxt
                if i == n * n:
                    return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    stack.append(i)
        return -1
