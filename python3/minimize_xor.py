class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = bin(num1)[2:]
        b2 = bin(num2)[2:]
        n1 = len(b1) 
        n2 = len(b2)
        n = max(n1, n2)

        if n1 < n:
            b1 = ('0' * (n - n1)) + b1

        ones = 0
        for bit in b2:
            if bit == '1':
                ones += 1

        bits = ['0' for _ in range(n)]
        for i in range(n):
            if ones == 0:
                break

            if b1[i] == '1':
                bits[i] = '1'
                ones -= 1

        j = n-1
        while ones > 0 and j >= 0:
            if bits[j] == '0':
                bits[j] = '1'
                ones -= 1
            j -= 1
            
        return int("".join(bits), 2)
        