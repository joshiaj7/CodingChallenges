"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            power, brain = questions[i]
            dp[i] = max(power + dp[min(n, i + brain + 1)], dp[i+1])

        return dp[0]
