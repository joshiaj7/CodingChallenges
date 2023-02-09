from collections import defaultdict

"""
Space   : O(n)
Time    : O(n ^ 2)
"""

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0
        count = defaultdict(set)

        for x in ideas:
            count[x[0]].add(hash(x[1:]))

        for a, seta in count.items():
            for b, setb in count.items():
                if a >= b:
                    continue

                same = len(seta & setb)
                ans += (len(seta) - same) * (len(setb) - same)

        return ans * 2
