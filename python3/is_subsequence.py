"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        i = 0
        for j in range(n):
            if i == m:
                return True

            if s[i] == t[j]:
                i += 1

        if i == m:
            return True
        
        return False
        
        