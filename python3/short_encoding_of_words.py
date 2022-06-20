class Trie:
    def __init__(self):
        self.d = {}
        self.leaves = []

    def insert(self, word):
        p = self.d
        for l in word:
            if l not in p:
                p[l] = {}
            p = p[l]

        # append leaf
        if len(p) == 0:
            self.leaves.append(word)

    def getLeaves(self):
        return self.leaves


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        Best solution
        Space   : O(n)
        Time    : O(n**2)    
        """
        word_set = set(words)
        for word in words:
            if word in word_set:
                for i in range(1, len(word)):
                    word_set.discard(word[i:])

        return len("#".join(list(word_set))) + 1

    def minimumLengthEncodingTrie(self, words: List[str]) -> int:
        """
        Space   : O(n)
        Time    : O(n**2)   
        """
        trie = Trie()

        words = list(set(words))
        words.sort(key=lambda w: -len(w))
        for word in words:
            trie.insert(word[::-1])

        return len("#".join(trie.getLeaves())) + 1
