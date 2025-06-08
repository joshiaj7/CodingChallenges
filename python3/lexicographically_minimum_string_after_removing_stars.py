from heapq import heappop, heappush

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def clearStars(self, s: str) -> str:
        ans = ""
        heap = []

        for i, l in enumerate(s):
            if l == "*":
                if not heap:
                    continue
                heappop(heap)
            else:
                heappush(heap, (l, -i))

        heap.sort(key=lambda x: -x[1])
        for l, _ in heap:
            ans += l

        return ans
