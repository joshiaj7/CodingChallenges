"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        ans = 0
        mem = ''

        for l in s:
            if l != mem:
                mem = l
                count = 1
            else:
                count += 1
            ans = max(ans, count)

        return ans
