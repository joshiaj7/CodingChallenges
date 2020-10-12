"""
Space   : O(n)
Time    : O(n)
"""

from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        dif = 0
        dupe = False
        ca, cb = Counter(A), Counter(B)
        n = len(A)

        # A must not be empty
        if n == 0:
            return False
        # A and B must have the same length
        if n != len(B):
            return False
        # A and B must have the same chars
        if len(ca - cb) > 0:
            return False

        # check if there's duplicate letter in A
        for k, v in ca.items():
            if v > 1:
                dupe = True
                break

        # get difference
        for idx in range(n):
            if A[idx] != B[idx]:
                dif += 1

        if dif == 0 and dupe:
            return True
        elif dif != 2:
            return False

        return True
