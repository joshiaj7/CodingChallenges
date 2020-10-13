"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        n = len(s)

        rev = True
        for i in range(0, n, k):
            chunk = s[i:i+k]

            if rev:
                ans += "".join(chunk[::-1])
                rev = False
            else:
                ans += "".join(chunk)
                rev = True

        return ans
