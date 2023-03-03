"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        
        s = ""
        count = 0
        for i in range(n):
            if i == 0:
                s += chars[i]
                count = 1
                continue

            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count > 1:
                    s += str(count)
                s += chars[i]
                count = 1
            
        if count > 1:
            s += str(count)

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)
