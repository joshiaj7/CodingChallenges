from heapq import heappush, heappop

# Space : O(n)
# Time  : O(n log n)


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans = 0
        fuels = []
        stations.append([target, 0])
        stations.insert(0, [0, 0])
        n = len(stations)

        for i in range(1, n):
            while startFuel < (stations[i][0] - stations[i-1][0]):
                if len(fuels) == 0:
                    return -1

                # if fuels is not empty
                startFuel += -heappop(fuels)
                ans += 1

            startFuel -= (stations[i][0] - stations[i-1][0])
            heappush(fuels, -stations[i][1])

            if target == stations[i][0]:
                break

        return ans
