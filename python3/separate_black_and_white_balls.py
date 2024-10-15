"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        n = len(s)

        i, j = 0, n-1
        while i < j:
            if s[j] == "1":
                j -= 1
                continue
            
            if s[i] == "0":
                i += 1
                continue
    
            ans += j - i
            i += 1
            j -= 1

        return ans
