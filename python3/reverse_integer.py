# leetcode

class Solution:
    def reverse(self, x: int) -> int:    
    
        str_x = str(x)
        if str_x[:1] == "-":
            isNeg = True
            str_x = str_x[1:]
        else:
            isNeg = False
            
        str_x = str_x[::-1]
        new_x = int(str_x)
        
        if isNeg:
            new_x *= -1
        
        if new_x < 2**31 * -1 or new_x > 2**31:
            return 0
        else:
            return new_x
    