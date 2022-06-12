from collections import defaultdict


"""
Space   : O(n)
Time    : O(n**2)
"""


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_map = defaultdict(list)
        n = len(beginWord)

        for word in wordList:
            for i in range(word):
                word_map[word[:i] + '*' + word[i + 1:]].append(word)

        q = [beginWord]
        transformations = 1
        visited = set([beginWord])

        while q:
            transformations += 1
            new_q = []
            for w1 in q:
                for i in range(n):
                    for w2 in word_map[w1[:i] + '*' + w1[i + 1:]]:
                        if w2 in visited:
                            continue
                        if w2 == endWord:
                            return transformations
                        new_q.append(w2)
                        visited.add(w2)

            q = new_q

        return 0
