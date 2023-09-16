from heapq import heappop, heappush
from typing import List


"""
Space   : O(mn)
Time    : O(mn log(mn))

method:
Djikstra algorithm to find shortest path
"""


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
      m, n = len(heights), len(heights[0])
      coord = [(0, 1), (1, 0), (0, -1),  (-1, 0)]
      heap = [(0, 0, 0)]
      visited = set()

      while heap:
        effort, i, j = heappop(heap)
        if (i, j) in visited:
          continue

        visited.add((i, j))
        if i + 1 == m and j + 1 == n:
          return effort

        for di, dj in coord:
          ni = i + di
          nj = j + dj
          if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
            neffort = max(effort, abs(heights[i][j] - heights[ni][nj]))
            heappush(heap, (neffort, ni, nj))

      return
