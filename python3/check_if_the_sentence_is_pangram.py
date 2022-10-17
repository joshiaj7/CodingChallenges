"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}

        for char in sentence:
            d[char] = 1

        return len(d) == 26
