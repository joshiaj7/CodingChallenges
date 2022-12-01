"""
Space   : O(1)
Time	: O(n)
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)

        start = n // 2
        end = n // 2
        if n % 2 == 0:
            start -= 1

        h1, h2 = 0, 0
        while start >= 0:
            if s[start] in vowels:
                h1 += 1
            
            if s[end] in vowels:
                h2 += 1

            start -= 1
            end += 1
        
        return h1 == h2
        
