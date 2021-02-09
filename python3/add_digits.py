"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        while len(str(num)) > 1:
            n = str(num)
            temp = 0
            for i in n:
                temp += int(i)
            num = temp

        return num
