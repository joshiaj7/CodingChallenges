from collections import Counter

"""
Space   : O(n)
Time    : O(m + n)
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hash table to store char frequency
        need = Counter(t)
        # total number of chars we care
        missing = len(t)
        start, end = 0, 0
        i = 0

        # index j from 1
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:  # match all chars
                # remove chars to find the real start
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                # make sure the first appearing char satisfies need[char]>0
                need[s[i]] += 1
                missing += 1  # we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  # update window
                    start, end = i, j
                i += 1  # update i to start+1 for next window
        return s[start:end]
