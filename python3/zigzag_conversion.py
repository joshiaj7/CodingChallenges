"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        makeWord = {}

        if numRows == 1:
            return s

        n = len(s)
        i = 0
        count = 1
        direction = '+'

        while i < n:
            if count not in makeWord:
                makeWord[count] = s[i]
            else:
                makeWord[count] += s[i]

            if count == 1:
                direction = '+'
            elif count == numRows:
                direction = '-'

            if direction == '+':
                count += 1
            elif direction == '-':
                count -= 1

            i += 1

        ans = ''
        for i in range(1, numRows+1):
            if i in makeWord:
                ans += makeWord[i]
            else:
                break

        return ans
