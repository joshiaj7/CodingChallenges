from typing import List

"""
Space   : O(n)
Time     :O(n)
"""

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = ""
        n = len(s)
        pref = [0 for _ in range(n)]

        for start, end, d in shifts:
            add = 1
            if d == 0:
                add = -1

            pref[start] += add
            if end+1 < n:
                pref[end+1] -= add

        for i in range(1, n):
            pref[i] += pref[i-1]
        
        for i in range(n):
            change = pref[i] % 26
            if change < 0:
                change += 26

            curr = ord(s[i]) - 97
            final = (curr + change) % 26

            ans += chr(final + 97)

        return ans
