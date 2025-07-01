"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1

        lastLetter = ""
        for l in word:
            if lastLetter == "":
                lastLetter = l
                continue

            if lastLetter != l:
                lastLetter = l
            else:
                ans += 1

        return ans
        