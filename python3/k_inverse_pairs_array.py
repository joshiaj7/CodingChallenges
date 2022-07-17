"""
Space   : O(nk)
Time    : O(nk)
"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        max_possible_inversions = (n * (n-1)) // 2
        if k > max_possible_inversions:
            return 0
        if k == 0 or k == max_possible_inversions:
            return 1

        dp = []
        for _ in range(n+1):
            temp = [0] * (k+1)
            temp[0] = 1
            dp.append(temp)

        dp[2][1] = 1

        for i in range(3, n+1):
            max_possible_inversions = min(k, (i * (i-1)) // 2)
            for j in range(max_possible_inversions+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if j >= i:
                    dp[i][j] -= dp[i-1][j-i]
                dp[i][j] %= 1000000007

        return dp[n][k]
