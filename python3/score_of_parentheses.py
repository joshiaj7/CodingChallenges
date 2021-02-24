"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = 0
        pwr = -1
        isAdded = False
        
        for l in S:
            if l == "(":
                pwr += 1 
                isAdded = False
            else:
                if not isAdded:
                    ans += 2 ** pwr
                    isAdded = True
                pwr -= 1
        
        return ans