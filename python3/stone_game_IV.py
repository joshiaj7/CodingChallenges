"""
Space   : O(n)
Time    : O(nk)
"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        square = []
        for x in range(1, int(n**0.5)+1):
            square.append(x**2)

        dp = [False] * (n+1)

        for i in range(1, n+1):
            for s in square:
                if s > i:
                    break
                if dp[i-s] == False:
                    dp[i] = True
                    break

        return dp[-1]
