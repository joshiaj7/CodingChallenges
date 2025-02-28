"""
Space   : O(n)
Time    : O(nm)
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = []
        m = len(part)

        for c in s:
            ans.append(c)
            if len(ans) >= m and "".join(ans[-m:]) == part:
                ans = ans[:len(ans)-m]

        return "".join(ans)
        