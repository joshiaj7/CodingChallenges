# leetcode

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        leng = len(digits)
        
        for i in range(leng-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
            if i == 0 and digits[i] == 0:
                digits[i] = 1
                digits += [0]
        
        return digits