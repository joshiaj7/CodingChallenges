"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        d = {}

        for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1

        mem = set()
        for v in d.values():
            while v > 0 and v in mem:
                v -= 1
                ans += 1
            mem.add(v)

        return ans
