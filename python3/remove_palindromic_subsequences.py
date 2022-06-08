"""
Space    : O(1)
Time     : O(n)
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[::-1]) - (s == "")
