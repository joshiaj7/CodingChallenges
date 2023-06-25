from typing import List
from functools import lru_cache

"""
Space   : O(n * fuel)
Time    : O(fuel * n ^ 2)
"""

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 1000000007
        n = len(locations)
        
        dp = [[0] * (fuel + 1) for _ in range(n)]
        for f in range(fuel + 1):
            dp[finish][f] = 1
        
        for f in range(fuel + 1):
            for city in range(n):
                for next_city in range(n):
                    if next_city != city and f >= abs(locations[next_city] - locations[city]):
                        dp[city][f] = (dp[city][f] + dp[next_city][f - abs(locations[next_city] - locations[city])]) % MOD
        
        return dp[start][fuel]

    def countRoutesRecurse(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        MOD = 10**9 +7
        
        @lru_cache
        def recur(i, fuel):
            if fuel < 0:
                return 0
            
            ans = 0 
            if i == finish:
                ans += 1
            
            for j in range(N):
                if j == i:
                    continue
                ans += recur(j, fuel - abs(locations[i] - locations[j]))
            
            return ans % MOD
        
        
        return recur(start, fuel)
