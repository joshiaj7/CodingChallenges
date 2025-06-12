from typing import List
from heapq import heappush, heappop

"""
Space   : O(nm)
Time    : O(nm log(nm))
"""

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        
        grid = [[-1 for _ in range(m)] for _ in range(n)]
        heap = []

        coord = [(0, 1), (1, 0), (0 ,-1),  (-1, 0)]

        # initial
        inputted = set((0, 0))
        heappush(heap, (0, 0, 0))

        while heap:
            val, i, j = heappop(heap)

            if i == 0 and j == 0:
                grid[i][j] = 0
            
            minNeighbor = float('inf')
            uninputtedNeighbors = []
            # check neighbor
            for di, dj in coord:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    # visited and processed
                    if grid[ni][nj] != -1:
                        minNeighbor = min(minNeighbor, grid[ni][nj] + 1)
                    # new node, never inputted
                    elif (ni, nj) not in inputted:
                        uninputtedNeighbors.append((ni, nj))

            if minNeighbor != float('inf'):
                grid[i][j] = max(minNeighbor, val)


            for ni, nj in uninputtedNeighbors:
                if grid[i][j] + 1 > moveTime[ni][nj]:
                    heappush(heap, (grid[i][j] + 1, ni, nj))
                else:
                    heappush(heap, (moveTime[ni][nj] + 1, ni, nj))
                inputted.add((ni, nj))

        return grid[n-1][m-1]




