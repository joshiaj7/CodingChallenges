from heapq import heappush, heappop

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        items = [(L, -H, R) for L, R, H in buildings]
        items += list({(R, 0, 0) for _, R, _ in buildings})
        items.sort()

        ans = [[0, 0]]
        heap = [(0, float('inf'))]

        for pos, neg_h, R in items:
            while heap[0][1] <= pos:
                heappop(heap)

            if neg_h:
                heappush(heap, (neg_h, R))

            if ans[-1][1] != -heap[0][0]:
                ans.append([pos, -heap[0][0]])

        return ans[1:]
