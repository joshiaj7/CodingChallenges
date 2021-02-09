"""
Space   : O(n)
Time    : O(n)
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dp = [0] * 1001
        pass_req = 0

        for trip in trips:
            dp[trip[1]] += trip[0]
            dp[trip[2]] -= trip[0]

        for i in dp:
            pass_req += i
            if pass_req > capacity:
                return False

        return True
