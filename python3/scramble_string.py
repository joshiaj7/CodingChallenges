"""
Space   : O(n^2)
Time    : O(4^n)
"""


class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]

        if n != m or sorted(s1) != sorted(s2):
            self.memo[(s1, s2)] = False
            return False

        if n < 4 or s1 == s2:
            self.memo[(s1, s2)] = True
            return True

        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True

        self.memo[(s1, s2)] = False
        return False
