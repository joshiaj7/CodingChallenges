from heapq import heappush, heappop

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        ans = []

        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1

        q = [(word, freq) for word, freq in d.items()]
        q.sort(key=lambda x: (-x[1], x[0]))

        for i in range(k):
            ans.append(q[i][0])

        return ans


"""
Space   : O(n)
Time    : O(n log k)
"""


class Comp:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    # built in less than function
    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution:
    def topKFrequentBest(self, words: List[str], k: int) -> List[str]:
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1

        h = []
        for key, val in d.items():
            heappush(h, (Comp(key, val), key))
            if len(h) > k:
                heappop(h)

        ans = []
        for i in range(k):
            val, key = heappop(h)
            ans.append(key)

        return ans[::-1]
