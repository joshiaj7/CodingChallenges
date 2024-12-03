from typing import List

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        m = len(spaces)

        w = ""
        j = 0
        for i, l in enumerate(s):
            if j < m and i == spaces[j]:
                words.append(w)
                w = ""
                j += 1

            w += l

        words.append(w)

        return " ".join(words)
        