"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = len(s)
        hs, ht = {}, {}

        for c in s:
            if c in hs:
                hs[c] += 1
            else:
                hs[c] = 1

        for c in t:
            if c in ht:
                ht[c] += 1
            else:
                ht[c] = 1

        for k, v in hs.items():
            if k in ht:
                ans -= min(v, ht[k])

        return ans
        