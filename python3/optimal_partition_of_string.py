"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        exists = set()

        for char in s:
            if char in exists:
                exists = set()
                ans += 1

            exists.add(char)
            
        return ans + 1
