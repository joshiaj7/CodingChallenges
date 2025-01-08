from typing import List

"""
Space   : O(1)
Time    : O(n^3)
"""


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):
                res = self.isPrefixAndSuffix(words[i], words[j])
                if res:
                    ans += 1

        return ans

    def isPrefixAndSuffix(self, a, b):
        lena = len(a)
        lenb = len(b)

        return b[:lena] == a and b[lenb-lena:] == a
