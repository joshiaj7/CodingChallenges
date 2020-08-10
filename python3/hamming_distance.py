# leetcode

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        xor = bin(x^y)[2:]
        
        for l in xor:
            if l == '1':
                ans += 1
            
        return ans