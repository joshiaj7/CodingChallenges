"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        temp = []
        n = len(A)

        for i in range(n):
            if i == 0:
                temp.append('-')
                continue
            if A[i] - A[i-1] > 0:
                temp.append('U')
            elif A[i] - A[i-1] == 0:
                temp.append('N')
            else:
                temp.append('D')

        up, down = False, False
        for j in range(n):
            if temp[j] == 'U' and not down:
                up = True
            elif temp[j] == 'D' and not up:
                return False
            elif temp[j] == 'U' and down:
                return False
            elif temp[j] == 'D' and up:
                down = True
            elif temp[j] == 'N':
                return False

        if not down:
            return False

        return True
