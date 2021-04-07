# Space : O(1)
# Time	: O(n/2)


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        v1, v2 = 0, 0
        
        for i in range(n//2):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                v1 += 1
            if s[i+(n//2)].lower() in ['a', 'e', 'i', 'o', 'u']:
                v2 += 1
        
        return v1 == v2
        
        
