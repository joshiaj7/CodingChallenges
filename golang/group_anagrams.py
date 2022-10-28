from collections import defaultdict

"""
Space   : O(n)
Time    : O(n * n log n)
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for w in strs:
            s = "".join(sorted(w))
            d[s].append(w)

        return d.values()
