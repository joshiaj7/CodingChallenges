from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        m = len(pref)

        for word in words:
            if word[:m] == pref:
                ans += 1

        return ans
