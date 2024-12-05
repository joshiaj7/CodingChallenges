"""
Space   : O(1)
Time    : O(n)
two pointers
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start += "#"
        target += "#"

        i = 0
        j = 0
        while i < n or j < n:
            while i < n and start[i] == "_":
                i += 1
            
            while j < n and target[j] == "_":
                j += 1

            if start[i] != target[j]: 
                return False
            elif start[i] == target[j] == "L" and i < j:
                return False
            elif start[i] == target[j] == "R" and i > j:
                return False

            i += 1
            j += 1

        return True
        