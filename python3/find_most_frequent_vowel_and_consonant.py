from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        letterMap = defaultdict(int)

        for l in s:
            letterMap[l] += 1

        maxVow = 0
        maxCons = 0
        for k, v in letterMap.items():
            if k in vowels:
                maxVow = max(maxVow, v)
            else:
                maxCons = max(maxCons, v)

        return maxVow + maxCons
    