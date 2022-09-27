"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        to_right, to_left = [-1] * n, [-1] * n
        ans = ""

        # populate to right direction
        r = -1
        for i in range(n):
            if dominoes[i] == 'R':
                r = i
                to_right[i] = 1
            elif dominoes[i] == 'L':
                r = -1
            elif r >= 0:
                to_right[i] = to_right[i-1] + 1

        # populate to left direction
        l = -1
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                l = i
                to_left[i] = 1
            elif dominoes[i] == 'R':
                l = -1
            elif l >= 0:
                to_left[i] = to_left[i+1] + 1

        # count everything
        for i in range(n):
            if to_right[i] == -1 and to_left[i] == -1:
                char = '.'
            elif to_right[i] == -1:
                char = 'L'
            elif to_left[i] == -1:
                char = 'R'
            elif to_right[i] < to_left[i]:
                char = 'R'
            elif to_right[i] > to_left[i]:
                char = 'L'
            else:
                char = '.'

            ans += char

        return ans
