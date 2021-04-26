from heapq import heappush, heappop

# Space : O(n)
# Time  : O(n * n log n)

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        h = []
        total = 0
        
        for i in range(1, n):
            dif = heights[i] - heights[i-1]
            if dif > 0:
                heappush(h, -dif)
                total += dif
            if total > bricks:
                if ladders > 0:
                    total += heappop(h)
                    ladders -= 1
                else:
                    return i-1
        
        return n-1
        