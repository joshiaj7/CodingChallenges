from collections import defaultdict, heapq

"""
Space   : O(n)
Time    : O(n)

Method:
Shortest path Djikstra
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, destination, val in times:
            graph[source].append((destination, val))

        ans = 0
        nodecount = 0
        heap = [(0, k)]
        visited = [False] * (n+1)
        distance = [float('inf')] * (n+1)

        while heap:
            curr_time, node = heapq.heappop(heap)
            if visited[node]:
                continue

            visited[node] = True
            nodecount += 1
            ans = max(ans, curr_time)

            for dest, time in graph[node]:
                if not visited[dest] and curr_time + time < distance[dest]:
                    distance[dest] = curr_time + time
                    heapq.heappush(heap, (curr_time + time, dest))

        if nodecount < n:
            return -1

        return ans
