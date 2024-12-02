"""
Space   : O(1)
Time    : O(nm)
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        m = len(searchWord)

        for i, v in enumerate(sentence.split(" ")):
            if v[:m] == searchWord:
                return i + 1

        return -1
