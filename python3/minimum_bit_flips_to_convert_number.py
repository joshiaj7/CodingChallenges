"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        xor = bin(start^goal)[2:]
        
        for l in xor:
            if l == '1':
                ans += 1
            
        return ans
        
        