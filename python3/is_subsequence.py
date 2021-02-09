# leetcode

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        mem = ''
        idx = 0
        
        for l in t:
            if l == s[idx]:
                idx += 1
                mem += l
            if idx == len(s):
                break
        
        if mem == s:
            return True
        else:
            return False
        
        
        