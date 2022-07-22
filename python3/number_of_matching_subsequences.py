from collections import defaultdict

"""
Space : O(n)
Time  : O(s * n)
where n = len(words)
"""


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        d = defaultdict(list)
        
        for w in words:
            d[w[0]].append(w[1:])
        
        for c in s:
            if c not in d:
                continue
            items = d.pop(c)
            for item in items:
                if len(item) == 0:
                    ans += 1
                else:
                    d[item[0]].append(item[1:])

        return ans
