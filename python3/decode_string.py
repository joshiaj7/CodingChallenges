"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def getString(self, n: int, s: str) -> str:
        ans = ''
        c, mul, start = 0, 0, 0

        for i in range(len(s)):
            if 48 <= ord(s[i]) <= 57:
                if c == 0:
                    mul = (mul * 10) + int(s[i])
            elif s[i] == '[':
                if c == 0:
                    start = i
                c += 1
            elif s[i] == ']':
                c -= 1
                if c == 0:
                    ans += self.getString(mul, s[start+1: i])
                    mul = 0
            elif c == 0:
                ans += s[i]

        return n * ans

    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return s

        return self.getString(1, s)
