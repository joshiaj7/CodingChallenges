from typing import List

"""
Space   : O(n)
Time    : O(nm)
"""



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = [False] * n

        for i in range(n):
            for w in wordDict:
                if w == s[i-len(w)+1 : i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True

        return d[-1]
