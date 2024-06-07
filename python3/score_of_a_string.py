"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(1, n):
            ans += abs(ord(s[i]) - ord(s[i-1]))

        return ans


        