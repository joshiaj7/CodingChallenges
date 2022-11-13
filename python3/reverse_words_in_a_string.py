"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        temp = []
        word = ""

        for c in s:
            if c == " ":
                if word:
                    temp = [word] + temp
                    word = ""
                continue

            word += c

        if word:
            temp = [word] + temp

        return " ".join(temp)