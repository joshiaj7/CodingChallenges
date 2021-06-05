from heapq import heappush, heappop

# Space : O(n)
# Time  : O(n log n)


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mem = []
        for i in range(n):
            mem.append((efficiency[i], speed[i]))

        mem.sort(key=lambda x: x[0], reverse=True)

        speed_heap = []
        speedTotal = 0
        ans = 0
        for i in range(n):
            heappush(speed_heap, mem[i][1])
            if len(speed_heap) <= k:
                speedTotal += mem[i][1]
            else:
                speedTotal += mem[i][1] - heappop(speed_heap)
            eff = mem[i][0]

            ans = max(ans, (eff * speedTotal))

        return ans % (10**9 + 7)
