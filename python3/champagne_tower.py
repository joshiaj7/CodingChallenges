"""
Space   : O(n)
Time    : O(n**2)
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * 100
        dp[0] = float(poured)

        for i in range(1, query_row + 1):
            for j in range(i-1, -1, -1):
                remain = (max(dp[j], 1.0) - 1.0) / 2.0
                dp[j+1] += remain
                dp[j] = remain

        return 1 if dp[query_glass] >= 1 else dp[query_glass]
