"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        max_dep, dep = 0, 0
        for i in range(n):
            if s[i] == '(':
                dep += 1
                max_dep = max(max_dep, dep)
            elif s[i] == ')':
                dep -= 1

        return max_dep
