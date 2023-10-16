from typing import List

"""
Space   : O(nk)
Time    : O(nk)
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]
        if rowIndex == 0:
            return pascal[-1]

        pascal.append([1, 1])
        if rowIndex == 1:
            return pascal[-1]

        for i in range(2, rowIndex+1):
            temp = [0] * (i + 1)
            temp[0] = 1
            n = len(temp)

            if n % 2 == 0:
                half = (n // 2) - 1
            else:
                half = (n // 2)

            # fill half of the triangle
            temp[0] = 1
            for j in range(1, half + 1):
                temp[j] = pascal[i-1][j-1] + pascal[i-1][j]

            if n % 2 == 0:
                half += 1

            for k in range(1, half + 1):
                temp[n - k] = temp[k-1]

            pascal.append(temp)

        return pascal[-1]
