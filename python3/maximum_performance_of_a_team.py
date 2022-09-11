from heapq import heappush, heappop

# Space : O(n)
# Time  : O(n log n)


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mem = [(i, j) for i, j in zip(efficiency, speed)]
        mem.sort(key=lambda x: -x[0])

        eng = []
        total_speed = 0
        ans = 0
        for eff, spd in mem:
            heappush(eng, spd)
            total_speed += spd

            if len(eng) > k:
                total_speed -= heappop(eng)

            ans = max(ans, total_speed * eff)

        return ans % 1000000007
