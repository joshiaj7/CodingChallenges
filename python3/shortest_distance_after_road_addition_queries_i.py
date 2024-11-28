from typing import List
from collections import defaultdict

"""
Space   : O(n)
Time    : O(qn)
graph
"""


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []

        graph = defaultdict(list)
        for i in range(n-1):
            graph[i].append(i+1)

        start = 0
        dest = n-1
        for u, v in queries:
            graph[u].append(v)

            step = 1
            sources = [start]
            visited = set()
            while True:
                end = False
                temp = []
                for neighs in sources:
                    for x in graph[neighs]:
                        if x in visited:
                            continue
                        if x == dest:
                            end = True
                            break
                        visited.add(x)
                        temp.append(x)

                if end or not temp:
                    break

                step += 1
                sources = temp

            ans.append(step)


        return ans
        