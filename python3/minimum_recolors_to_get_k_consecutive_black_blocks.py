"""
Space   : O(1)
Time    : O(n)
Sliding window
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = 100
        n = len(blocks)
        left = 0

        whites = 0
        for i in range(k):
            if blocks[i] == "W":
                whites += 1

        ans = min(ans, whites)
        for i in range(k, n):
            if blocks[i] == "W":
                whites += 1
            if blocks[left] == "W":
                whites -= 1
            left += 1
            ans = min(ans, whites)

        return ans
        