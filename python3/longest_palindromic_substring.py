"""
Space   : O(1)
Time    : O(n**2)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        i, mx, st = 0, 0, 0

        while i < n:
            curr = 0
            start = i
            end = i

            while ((end + 1) < n) and (s[end] == s[end+1]):
                end += 1
            i = end + 1

            while ((end + 1) < n) and ((start - 1) >= 0) and (s[start-1] == s[end+1]):
                start -= 1
                end += 1

            curr = (end - start) + 1
            if curr > mx:
                mx = curr
                st = start

        ans = s[st:st+mx]
        return ans
