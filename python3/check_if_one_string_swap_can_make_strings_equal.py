from collections import defaultdict

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n != m:
            return False

        diff = 0
        diff_s1 = defaultdict(int)
        diff_s2 = defaultdict(int)
        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1
                diff_s1[s1[i]] += 1
                diff_s2[s2[i]] += 1

            if diff > 2:
                return False

        if diff == 1:
            return False

        for k, v in diff_s1.items():
            if k not in diff_s2:
                return False

        return True
        