# Space : O(1)
# Time  : O((n log n) ^ 2)

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda word: [order.index(c) for c in word])
