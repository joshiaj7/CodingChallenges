"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n + 1):
            # check current 1 digit
            if 0 < int(s[i-1]) <= 9:
                dp[i] += dp[i-1]

            # check 2 digits
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]
