"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # forward
        start, par = 0, 0
        for end in range(n):
            if s[end] == "(":
                par += 1
            else:
                par -= 1
                
            if par < 0:
                start = end + 1
                par = 0
            elif par == 0:
                ans = max(ans, end-start+1)
            
        # backward
        end, par = n-1, 0
        for start in range(n-1, -1, -1):
            if s[start] == "(":
                par += 1
            else:
                par -= 1
                
            if par > 0:
                end = start - 1
                par = 0
            elif par == 0:
                ans = max(ans, end-start+1)
                
        return ans