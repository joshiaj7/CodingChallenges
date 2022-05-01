"""
Space	: O(n)
Time	: O(n)

Mehtod:
Stack
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s):
            a = []
            n = len(s)
            for i in range(n):
                if s[i] == '#':
                    if a:
                        a.pop()
                else:
                    a.append(s[i])
            return a

        return process(s) == process(t)
