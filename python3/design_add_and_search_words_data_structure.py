from collections import defaultdict

"""
Space   : O(n*m)
Time    : O(n*m)
"""

class WordDictionary:

    def __init__(self):
        self.trie = defaultdict(dict)
        
    def addWord(self, word: str) -> None:
        word += "#"
        p = self.trie
        for c in word:
            if c not in p:
                p[c] = defaultdict(dict)
            p = p[c]

    def search(self, word: str) -> bool:
        p = self.trie
        self.ans = False
        word += "#"
        self.dfs(p, word)
        return self.ans

    def dfs(self, pointer, word):
        if self.ans == True:
            return 

        if word[0] == "#" and "#" in pointer:
            self.ans = True
            return

        if word[0] in pointer:
            self.dfs(pointer[word[0]], word[1:])
        elif word[0] == ".":
            for k, v in pointer.items():
                self.dfs(v, word[1:])
