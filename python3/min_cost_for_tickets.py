# leetcode

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        num = 366
        one, seven, thirty = costs
        dp = [0] * num
        idx = 0
        
        for i in range(1, num):
            dp[i] = dp[i-1]
            
            if i == days[idx]:
                # print("idx : {}, days : {}".format(idx, days[idx]))
                dp[i] = min(
                    one+dp[i-1 if i-1>0 else 0], 
                    seven+dp[i-7 if i-7>0 else 0], 
                    thirty+dp[i-30 if i-30>0 else 0]
                )
                
                if idx != len(days)-1:
                    idx += 1
                else:
                    break     
        
        # print(dp)
        # print(dp[days[idx]])
        return dp[days[idx]]
        