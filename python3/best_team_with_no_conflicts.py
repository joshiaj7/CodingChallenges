"""
Space   : O(max(age))
Time    : O(n log n)
"""

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        dp = [0] * (max(ages)+1)
        p = sorted(zip(scores, ages))

        for score, age in p:
            dp[age] = score + max(dp[:age+1])

        return max(dp)
