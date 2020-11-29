"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        n = len(arr)

        while stack:
            idx = stack.pop()
            if arr[idx] == 0:
                return True
            elif arr[idx] == -1:
                continue

            # visited
            val = arr[idx]
            arr[idx] = -1

            # minus
            if idx - val >= 0:
                stack.append(idx - val)

            # plus
            if idx + val < n:
                stack.append(idx + val)

        return False
