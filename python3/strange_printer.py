"""
Space   : O(n ^ 2)
Time    : O(n ^ 3)
"""

class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}

        def check(i, j):
            if (i, j) not in memo:
                if i > j:
                    return 0

                res = check(i, j-1) + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        res = min(res, check(i, k-1) + check(k, j-1))
                memo[(i, j)] = res
            return memo[(i, j)]

        # reduce s
        s = ''.join(a for a, b in zip(s, '#' + s) if a != b)
        return check(0, len(s) - 1)
