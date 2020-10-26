"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        stack = []

        i = 0
        while i < n:
            if arr[i] == 0:
                stack.append(0)
            stack.append(arr[i])
            i += 1

        for j in range(n):
            arr[j] = stack[j]
