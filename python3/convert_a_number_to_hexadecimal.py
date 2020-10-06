"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def getHex(self, num: int) -> str:
        ans = ''
        multi = 1

        while multi * 16 <= num:
            multi *= 16

        while multi >= 1:
            print("multi : {}".format(multi))

            temp = int(num // multi)

            if temp < 10:
                ans += str(temp)
            else:
                ans += chr(temp + 87)
            num %= multi
            multi /= 16

        return ans

    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        if num < 0:
            # ffffffff
            base = 4294967295
            num = base + num + 1

        return self.getHex(num)
