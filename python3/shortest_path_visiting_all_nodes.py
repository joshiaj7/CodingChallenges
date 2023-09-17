from typing import List
from math import inf

"""
Space   : O(n^2)
Time    : O(n!)
"""

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        masks = [1 << i for i in range(n)]
        all_visited = (1 << n) - 1
        q = [(i, masks[i]) for i in range(n)]
        steps = 0

        visited_states = [{masks[i]} for i in range(n)]

        while q:
            count = len(q)

            while count:
                current_node, visited = q[0]
                q = q[1:]
                if visited == all_visited:
                    return steps
                
                for new_node in graph[current_node]:
                    new_visited = visited | masks[new_node]

                    if new_visited == all_visited:
                        return steps + 1

                    if new_visited not in visited_states[new_node]:
                        visited_states[new_node].add(new_visited)
                        q.append((new_node, new_visited))

                count -= 1
            steps += 1

        return inf
        