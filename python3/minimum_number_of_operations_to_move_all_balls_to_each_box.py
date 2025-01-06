from typing import List

"""
Space   : O(n)
Time    : O(n^2)
"""

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        n = len(boxes)

        idxs = []
        for i in range(n):
            if boxes[i] == '1':
                idxs.append(i)

        for i in range(n):
            moves = 0
            for j in idxs:
                moves += abs(i-j)
            ans.append(moves)

        return ans
        