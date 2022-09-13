"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check_byte(byte, data):
            if len(data) != byte-1:
                return False

            for x in data:
                binary = format(x, '08b')
                if binary[:2] != '10':
                    return False

            return True

        n = len(data)
        i = 0
        while i < n:
            binary = format(data[i], '08b')
            res = True
            if binary[:1] == '0':
                i += 1
            elif binary[:3] == '110':
                res = check_byte(2, data[i+1:i+2])
                i += 2
            elif binary[:4] == '1110':
                res = check_byte(3, data[i+1:i+3])
                i += 3
            elif binary[:5] == '11110':
                res = check_byte(4, data[i+1:i+4])
                i += 4
            else:
                return False

            if i > n or not res:
                return False

        return True
