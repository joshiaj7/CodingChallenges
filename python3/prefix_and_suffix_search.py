from collections import defaultdict

"""
Space   : O(n**2)
Time    : O(n**2)

Mehtod:
Substring transversal
"""


class WordFilter:
    def __init__(self, words: List[str]):
        self.pre = defaultdict(set)
        self.suf = defaultdict(set)
        self.index = {}

        for i, w in enumerate(words):
            self.pre[''].add(w)
            self.index[w] = i
            for j in range(len(w)):
                self.pre[w[:j+1]].add(w)
            for j in range(len(w)-1, -1, -1):
                self.suf[w[j:]].add(w)

    def f(self, prefix: str, suffix: str) -> int:
        ans = -1
        for x in self.pre[prefix] & self.suf[suffix]:
            ans = max(ans, self.index[x])
        return ans
