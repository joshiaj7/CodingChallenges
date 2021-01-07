"""
Space   : O(1)
Time    : O(log n)
"""

import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <=1:
            return False
        
        total = 1
        
        s, e = 2, math.ceil(math.sqrt(num))
        
        while s < e:
            if num % s == 0:
                total += s
                total += num // s
            s += 1
    
        return total == num