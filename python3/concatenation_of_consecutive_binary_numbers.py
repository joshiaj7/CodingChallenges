"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        mod = 10**9 + 7
        power = 2
        shift = 1

        for i in range(1, n+1):
            if i == power:
                power *= 2
                shift += 1
            ans = ((ans << shift) + i) % mod

        return ans
