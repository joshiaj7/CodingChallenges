"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        truth = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }

        n = len(str(num))
        multi = 10 ** (n-1)

        for i in range(n):
            temp = int(str(num)[i])

            while temp > 0:
                if temp == 9:
                    ans += truth[9 * multi]
                    temp -= 9
                elif temp >= 5:
                    ans += truth[5 * multi]
                    temp -= 5
                elif temp >= 4:
                    ans += truth[4 * multi]
                    temp -= 4
                elif temp >= 1:
                    ans += truth[1 * multi]
                    temp -= 1

            multi //= 10

        return ans
