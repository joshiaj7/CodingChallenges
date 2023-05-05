"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        vow = 0
        n = len(s)

        def is_vowel(c):
            if c in {"a", "e", "i", "o", "u"}:
                return True
            return False

        for i in range(k):
            if is_vowel(s[i]):
                vow += 1
        ans = vow

        for i in range(k, n):
            # check head
            if is_vowel(s[i]):
                vow += 1

            # check tail
            if is_vowel(s[i-k]):
                vow -= 1

            ans = max(ans, vow)


        return ans
