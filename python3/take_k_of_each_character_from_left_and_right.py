from collections import defaultdict

"""
Space   : O(1)
Time    : O(n)
Sliding window
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        d = defaultdict(int)

        def isFulfilled(d, k):
            return d['a'] >= k and d['b'] >= k and d['c'] >= k

        # populate
        for v in s:
            d[v] += 1

        # validate
        if not isFulfilled(d, k):
            return -1

        # eliminate middle
        left = 0        
        for right in range(n):
            d[s[right]] -= 1

            if not isFulfilled(d, k):
                d[s[left]] += 1
                left += 1

        return n - (right - left  + 1)
