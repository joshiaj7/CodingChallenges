"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        mod = 10 ** 9 + 7

        for i in range(2, n + 1):
            ans = ans * (i * 2 - 1) * i % mod

        return ans
