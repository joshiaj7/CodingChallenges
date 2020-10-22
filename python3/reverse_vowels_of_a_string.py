"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        b, e = 0, (len(s)-1)

        s = list(s)
        while b < e:
            b_get, e_get = False, False

            if s[b].lower() in ['a', 'e', 'i', 'o', 'u']:
                b_get = True

            if s[e].lower() in ['a', 'e', 'i', 'o', 'u']:
                e_get = True

            if b_get and e_get:
                temp = s[b]
                s[b] = s[e]
                s[e] = temp
                b += 1
                e -= 1
            if not b_get:
                b += 1
            if not e_get:
                e -= 1

        return ''.join(s)
