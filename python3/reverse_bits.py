class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = bin(n)[2:]
        leng = len(n_bin)
        res = ''
        
        n_bin = '0' * (32-leng) + n_bin
        for i in range(31, -1, -1):
            res += n_bin[i]
        
        return int(res,2)