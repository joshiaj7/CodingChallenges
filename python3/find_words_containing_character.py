from typing import List

"""
Space   : O(1)
Time    : O(nm)
"""


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        n = len(words)

        for i in range(n):
            if x in words[i]:
                ans.append(i)
            
        return ans
        