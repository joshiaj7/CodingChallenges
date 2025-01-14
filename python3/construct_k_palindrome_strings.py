from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        
        d = defaultdict(int)
        for l in s:
            d[l] += 1

        odds = 0
        for v in d.values():
            if v % 2 == 1:
                odds += 1

        if odds > k:
            return False

        return True
        