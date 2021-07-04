# Space : O(1)
# Time  : O(1)

class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ ((2 ** len(bin(num)[2:]))-1)
