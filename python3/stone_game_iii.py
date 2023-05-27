"""
Space   : O(3)
Time    : O(n)
"""


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3

        for i in range(n-1, -1, -1):
            vals = []
            for k in range(1, 4):
                vals.append(sum(stoneValue[i:i + k]) - dp[(i + k) % 3])
            dp[(i%3)] = max(vals)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
