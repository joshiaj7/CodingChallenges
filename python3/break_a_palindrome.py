"""
Space : O(n)
Time  : O(n)
"""

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:     
        n = len(palindrome)
        if n == 1:
            return ""
        
        odd = True if n % 2 == 1 else False
        mid = n // 2
        d = {}
        
        for l in palindrome:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1
        
        if len(d) == 1:
            if palindrome[0] == 'a':
                return palindrome[:n-1] + 'b'
            else:
                return 'a' + palindrome[1:]
        
        for i in range(n):
            if odd and i == mid:
                continue
            
            order = ord(palindrome[i])
            if order > 97:
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        if palindrome[0] == 'a':
            return palindrome[:n-1] + 'b'

        return 'a' + palindrome[1:]
