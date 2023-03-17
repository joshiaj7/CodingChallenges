from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Trie:
    def __init__(self):
        self.d = defaultdict(dict)

    def insert(self, word: str) -> None:
        p = self.d
        word += "#"
        for c in word:
            if c not in p:
                p[c] = defaultdict(dict)
            p = p[c]

    def search(self, word: str) -> bool:
        p = self.d
        word += "#"
        for c in word:
            if c not in p:
                return False
            p = p[c]

        return True
        
    def startsWith(self, prefix: str) -> bool:
        p = self.d
        for c in prefix:
            if c not in p:
                return False
            p = p[c]

        return True
