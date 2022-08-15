"""
Space : O(7)
Time  : O(n)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        romanmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        n = len(s)
        ans = 0

        for idx in range(n-1):
            if romanmap[s[idx]] >= romanmap[s[idx+1]]:
                ans += romanmap[s[idx]]
            else:
                ans -= romanmap[s[idx]]

        ans += romanmap[s[-1]]
        return ans
