"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        brokenMap = {}

        for l in brokenLetters:
            brokenMap[l] = True

        for word in text.split(" "):
            typeable = True

            for l in word:
                if l in brokenMap:
                    typeable = False
                    break

            if typeable:
                ans += 1

        return ans
        