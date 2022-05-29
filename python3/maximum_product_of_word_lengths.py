"""
Space : O(n)
Time  : O(n**2)

method:
bitmask manipulation
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        bitmask = {}

        for w in words:
            bit = 0
            for l in w:
                bit |= (1 << (ord(l) - 97))
            bitmask[w] = bit

        for i in range(n):
            for j in range(i+1, n):
                if bitmask[words[i]] & bitmask[words[j]] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
