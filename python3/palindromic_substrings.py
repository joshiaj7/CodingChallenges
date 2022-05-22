"""
Space   : O(1)
Time    : O(n)

Method:
Palindrome stack
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 0

        while i < n:
            start, end = i, i
            ans += 1

            # expand forward if next char is equal
            while (end + 1 < n) and (s[end] == s[end + 1]):
                end += 1
                ans += 1

            # expand start and end if char at start and end are equal
            while (end + 1 < n) and (start - 1 >= 0) and (s[start-1] == s[end+1]):
                end += 1
                start -= 1
                ans += 1

            i += 1

        return ans
