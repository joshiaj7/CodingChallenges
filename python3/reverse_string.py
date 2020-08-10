# leetcode

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        dup = s.copy()
        
        idx = 0
        
        while idx < len(s):
            s[idx] = dup[len(s) - 1 - idx]
            idx += 1
            
        print(s)
            