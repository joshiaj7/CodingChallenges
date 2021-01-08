"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1, s2 = '', ''

        for x in word1:
            s1 += x

        for y in word2:
            s2 += y

        return s1 == s2
