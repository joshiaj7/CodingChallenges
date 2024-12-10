from collections import defaultdict

"""
Space   : O(n^2)
Time    : O(n^2)
"""

class Solution:
    def maximumLength(self, s: str) -> int:
        ans = 0
        n = len(s)
        d = defaultdict(int)

        for i in range(n):
            x = ''
            j = i

            while j < n and s[j] == s[i]:
                x += s[j]
                d[x] += 1      
                j += 1       

        for k, v in d.items():
            if v >= 3:
                ans = max(ans, len(k))

        return ans if ans > 0 else -1
