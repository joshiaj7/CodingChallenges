"""
Space   : O(n)
Time    : O(n)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        dp = []

        for i in range(N):
            dp.append(gas[i] - cost[i])

        if sum(dp) < 0:
            return -1

        temp = 0
        ans = -1

        for idx in range(N):
            temp += dp[idx]
            if temp >= 0 and ans == -1:
                ans = idx
            if temp < 0:
                ans = -1
            temp = max(temp, 0)

        return ans
