# leetcode

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False 
        ones = 0
        
        binary = bin(n)[2:]
        print(binary)
        
        for i in binary:
            if i == "1":
                ones += 1
        
        if ones == 1:
            return True
        else:
            return False
        