"""
Space   : O(n)
Time    : O(n)
n = biggest day
"""


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1] + 1
        dp = [0] * n

        j = 0
        for i in range(n):
            if i == days[j]:
                days1 = dp[i-1] + costs[0]
                days7 = dp[max(i-7, 0)] + costs[1]
                days30 = dp[max(i-30, 0)] + costs[2]

                dp[i] = min(days1, days7, days30)
                j += 1
            elif i > 0:
                dp[i] = dp[i-1]
            


        return dp[-1]
