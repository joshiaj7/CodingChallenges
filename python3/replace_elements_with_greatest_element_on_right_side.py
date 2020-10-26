"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        if n == 1:
            return [-1]

        temp = [0] * n

        for i in range(n-1, -1, -1):
            if i == n-1:
                temp[i] = -1
                continue
            temp[i] = max(temp[i+1], arr[i+1])

        return temp
