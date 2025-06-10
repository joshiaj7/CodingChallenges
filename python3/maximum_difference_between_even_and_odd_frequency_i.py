class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}

        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1

        minOdd, maxOdd = 100, 0
        minEven, maxEven = 100, 0 
        for v in d.values():
            if v % 2 == 0:
                minEven = min(minEven, v)
                maxEven = max(maxEven, v)
            else:
                minOdd = min(minOdd, v)
                maxOdd = max(maxOdd, v)

        return max((maxOdd - minEven), (minOdd - maxEven))
