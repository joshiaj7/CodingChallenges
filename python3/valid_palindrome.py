# leetcode

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cp = s.replace(" ", "").lower()
        
        clean_s = ''
        
        for l in s_cp:
            # check if num
            if ord(l) >= 48 and ord(l) <= 57:
                clean_s += l
            elif ord(l) >= 97 and ord(l) <= 122:
                clean_s += l
            
        return clean_s == clean_s[::-1]
