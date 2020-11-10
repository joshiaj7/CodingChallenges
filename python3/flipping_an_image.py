"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for y in range(len(A)):
            for x in range(len(A[0])):
                if A[y][x] == 0:
                    A[y][x] = 1
                else:
                    A[y][x] = 0

        B = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])-1, -1, -1):
                temp.append(A[i][j])
            B.append(temp)

        return B
