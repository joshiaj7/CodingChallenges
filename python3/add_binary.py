class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        len_a = len(a)
        len_b = len(b)
        store = 0
        
        if len_a > len_b:
            b = ('0' * (len_a - len_b)) + b
            len_b = len_a
        elif len_a < len_b:
            a = ('0' * (len_b - len_a)) + a
            len_a = len_b
        
        for i in range(len_a-1, -1, -1):
            total = store + int(a[i]) + int(b[i])
            if total < 2:
                store = 0
            elif total >= 2:
                store = 1
            res = str(total % 2) + res
            
        if store == 1:
            res = str(store) + res
        
        return res
        