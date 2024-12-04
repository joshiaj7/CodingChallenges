"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        i, j = 0, 0

        while i < n and j < m:
            ord1 = (ord(str1[i]) - 97 + 1) % 26
            ord2 = (ord(str2[j]) - 97)
            if str1[i] == str2[j] or ord1 == ord2:
                j += 1
            i += 1

        if j < m:
            return False

        return True
        