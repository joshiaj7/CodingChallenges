from typing import List

"""
Space   : O(n)
Time    : O(n^2)
"""

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        max_val = n + 1
        dp = [max_val] * (n + 1)
        dp[0] = 0
        d = set(dictionary)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            for j in range(1, i + 1):
                if s[i-j:i] in d:
                    dp[i] = min(dp[i], dp[i-j])

        return dp[-1]
        