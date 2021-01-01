"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {}
        n = len(arr)

        for x in pieces:
            if x[0] not in d:
                d[x[0]] = x

        i = 0
        while i < n:
            if arr[i] in d:
                temp = d[arr[i]]
                for j in range(len(temp)):
                    if temp[j] == arr[i]:
                        i += 1
                    else:
                        return False
            else:
                return False

        return True
