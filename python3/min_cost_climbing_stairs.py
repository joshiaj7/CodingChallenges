# leetcode

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        leng = len(cost)
        dp = [0] * leng
        
        for idx in range(leng):
            if idx < 2:
                dp[idx] = cost[idx]
            else:
                dp[idx] = cost[idx] + min(dp[idx-1], dp[idx-2])
            idx += 1
                
        print(dp)
        return min(dp[leng-1], dp[leng-2])