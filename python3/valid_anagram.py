"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd, td = {}, {}
        
        for l in s:
            if l in sd:
                sd[l] += 1
            else:
                sd[l] = 1
        
        for l in t:
            if l in td:
                td[l] += 1
            else:
                td[l] = 1
        
        return sd == td
