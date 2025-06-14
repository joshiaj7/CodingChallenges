"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minMaxDifference(self, num: int) -> int:
        biggest = 0
        smallest = 0

        s = str(num)

        # get biggest
        big = ""
        for l in s:
            if l == "9":
                continue 
            big = l
            break
        
        if big == "":
            biggest = num
        else:
            temp = ""
            for l in s:
                if l == big:
                    temp += "9"
                else:
                    temp += l
            biggest = int(temp)

        # get smallest
        small = s[0]
        temp = ""
        for l in s:
            if l == small:
                temp += "0"
            else:
                temp += l
        smallest = int(temp)

        return biggest - smallest
