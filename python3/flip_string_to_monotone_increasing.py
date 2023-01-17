"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zeros = s.count('0')
        ones = 0
        ans = n - zeros
        
        for i in range(n):
            if s[i] == '0':
                zeros -= 1
            else:
                ans = min(ans, zeros + ones)
                ones += 1

        return ans
