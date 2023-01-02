"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n == 1:
            return True

        if ord(word[0]) >= 97 and ord(word[1]) >= 97:
            form = 1 # all lower
        elif 65 <= ord(word[0]) <= 90:
            if 65 <= ord(word[1]) <= 90:
                form = 2 # all upper
            else:
                form = 3 # first upper
        else:
            return False

        for i in range(2, n):
            asc = ord(word[i])
            if form == 1 or form == 3:
                if asc < 97:
                    return False
            elif form == 2:
                if  asc >= 97:
                    return False
                
        return True
