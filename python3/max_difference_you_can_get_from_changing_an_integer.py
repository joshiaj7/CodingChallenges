"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        biggest = 0
        smallest = 0

        s = str(num)
        n = len(s)

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
        small = 0
        i = 0
        while i < n and s[i] in ["0", "1"]:
            i += 1
        
        if i < n:
            small = s[i] 

        changeTo = "0"
        if s[0] != "1":
            changeTo = "1"

        temp = ""
        for l in s:
            if l == small:
                temp += changeTo
            else:
                temp += l
        smallest = int(temp)

        return biggest - smallest
