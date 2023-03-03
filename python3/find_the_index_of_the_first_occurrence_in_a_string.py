"""
Space   : O(1)
Time    : O(hn)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hn, nn = len(haystack), len(needle)
        if nn > hn:
            return -1

        idx = -1
        j = 0
        for i in range(hn):
            while i < hn and haystack[i] == needle[j]:
                if idx == -1:
                    idx = i 
                if j == nn-1:
                    return idx 
                i += 1
                j += 1
            
            idx = -1
            j = 0 
            i += 1

        return -1
