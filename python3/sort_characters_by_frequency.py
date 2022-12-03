from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        ans = ""

        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        counter = defaultdict(list)
        for k, v in d.items():
            counter[v].append(k)    


        vals = sorted(list(counter.keys()), reverse=True)
        for i in vals:
            for c in counter[i]:
                ans += c * i

        return ans
