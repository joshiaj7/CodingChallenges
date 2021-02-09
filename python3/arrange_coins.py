"""
Space   : O(1)
Time    : O(n)
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans, count = 0, 0
        add = 1

        while count < n:
            count += add
            add += 1
            ans += 1
            
        if count > n:
            ans -= 1
        
        return ans