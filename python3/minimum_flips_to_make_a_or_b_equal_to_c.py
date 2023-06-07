"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        def toBin(x):
            return bin(x)[2:]

        bin_a = toBin(a)
        bin_b = toBin(b)
        bin_c = toBin(c)

        n = max(len(bin_a), len(bin_b), len(bin_c))
        
        if len(bin_a) < n:
            bin_a = '0' * (n - len(bin_a)) + bin_a
        if len(bin_b) < n:
            bin_b = '0' * (n - len(bin_b)) + bin_b
        if len(bin_c) < n:
            bin_c = '0' * (n - len(bin_c)) + bin_c

        for i in range(n):
            if bin_c[i] == '1':
                if bin_a[i] == '0' and bin_b[i] == '0':
                    ans += 1
            else:
                if bin_a[i] == '1':
                    ans +=1
                if bin_b[i] == '1':
                    ans +=1
                
        return ans
