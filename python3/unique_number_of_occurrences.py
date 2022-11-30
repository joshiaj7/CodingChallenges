"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for x in arr:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        vals = list(d.values())
        return len(vals) == len(set(vals))
