"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = ""
        alphabets = [0] * 26

        for l in s:
            alphabets[ord(l) - 97] += 1


        i = 25
        for i in range(25, -1, -1):
            if alphabets[i] == 0:
                continue

            while alphabets[i] > 0:
                if alphabets[i] <= repeatLimit:
                    ans += chr(i + 97) * alphabets[i]
                    alphabets[i] = 0
                    break

                ans += chr(i + 97) * repeatLimit
                alphabets[i] -= repeatLimit

                # borrowing alphabet
                j = i - 1
                while j >= 0 and alphabets[j] == 0:
                    j -= 1

                if j == -1:
                    break

                ans += chr(j + 97)
                alphabets[j] -= 1


        return ans
        