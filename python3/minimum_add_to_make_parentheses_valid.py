"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0

        count = 0
        for c in s:
            if c == "(":
                count += 1
            else:
                count -= 1

            if count < 0:
                ans += 1
                count = 0

        return ans + count
        