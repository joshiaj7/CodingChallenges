"""
Space   : O(n + m)
Time    : O(n + m)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n, m = len(word1), len(word2)
        i, j = 0, 0

        sign = 1
        while i < n and j < m:
            if sign == 1:
                ans += word1[i]
                i += 1
                sign = 0
            else:
                ans += word2[j]
                j += 1
                sign = 1

        if i < n:
            ans += word1[i:]

        if j < m:
            ans += word2[j:]

        return ans
