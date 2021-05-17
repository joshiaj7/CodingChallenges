# Space : O(n)
# Time  : O(len(word) * max len(word[i]))

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        predecessors = {w:1 for w in words}
        max_length = 1
        for w1 in words:
            for i in range(len(w1)):
                w2 = w1[:i]+w1[i+1:]
                if w2 in predecessors:
                    predecessors[w1] = max(predecessors[w2] + 1, predecessors[w1])
            if predecessors[w1] > max_length:
                max_length = predecessors[w1]

        return max_length