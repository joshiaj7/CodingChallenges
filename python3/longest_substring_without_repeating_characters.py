"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = 0
        d = {}
        
        for i, x in enumerate(s):
            if x in d and start <= d[x]:
                start = d[x]+1
            else:
                ans = max(ans, i - start+1)
            d[x] = i
    
        return ans