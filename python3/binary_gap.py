# Space : O(1)
# Time  : O(bin len)

class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        b = bin(n)[2:]

        s = 0
        b_len = len(b)
        for i in range(1, b_len):
            if b[i] == '1':
                ans = max(ans, i-s)
                s = i

        return ans
