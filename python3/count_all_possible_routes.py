from typing import List

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
