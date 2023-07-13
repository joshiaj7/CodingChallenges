from typing import List
from collections import defaultdict

"""
Space   : O(m)
Time    : O(m)

m = len(prerequisites)
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep = set()
        outdeg = defaultdict(int)
        prereq_graph = defaultdict(list)
    
        for u, v in prerequisites:
            dep.add(u)
            prereq_graph[v].append(u)
            outdeg[u] += 1

        queue = []
        for i in range(numCourses):
            if i not in dep:
                queue.append(i)

        visited = set()
        while queue:
            node = queue.pop(0)

            visited.add(node)
            for i in prereq_graph[node]:
                outdeg[i] -= 1
                if outdeg[i] == 0:
                    queue.append(i)
        

        return len(list(visited)) == numCourses
