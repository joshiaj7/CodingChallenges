from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        d = {}

        for c in allowed:
            d[c] = 1

        for word in words:
            w = list(set(list(word)))
            isAllowed = True
            for c in w:
                if c not in d:
                    isAllowed = False
                    break

            if isAllowed: 
                ans += 1

        return ans
