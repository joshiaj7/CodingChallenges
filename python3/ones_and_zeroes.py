"""
Space   : O(M * N)
Time    : O(strs  * M * N)

Method:
DP approach
bottom up
"""


class Solution:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros
            for i in range(M, zeros-1, -1):
                for j in range(N, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)

        return dp[M][N]
