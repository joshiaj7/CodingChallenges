from typing import List

"""
Space   : O(n)
Time    : O(nm)
"""

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        rot = [["" for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                rot[j][m - 1 - i] = box[i][j]

        for i in range(m):
            swappable = []
            for j in range(n-1, -1, -1):
                if rot[j][i] == ".":
                    swappable.append((j, i))
                elif rot[j][i] == "*":
                    swappable = []
                elif rot[j][i] == "#":
                    if swappable:
                        jj, ii = swappable.pop(0)
                        rot[j][i] = "."
                        rot[jj][ii] = "#"
                        swappable.append((j, i))

        return rot
