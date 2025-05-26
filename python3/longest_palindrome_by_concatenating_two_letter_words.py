from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        mid = False
        d = {}
        visited = set()

        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1

        for k, v in d.items():
            if k in visited:
                continue

            mirrored = k[::-1]
            if k == mirrored:
                if v % 2 == 1:
                    if not mid:
                        mid = True
                    ans += (v - 1) * 2
                else:
                    ans += v * 2
            elif mirrored in d:
                ans += min(v, d[mirrored]) * 4
                visited.add(mirrored)

        if mid:
            ans += 2

        return ans
