from typing import List

"""
Space   : O(V) + O(E)
Time    : O(V + E)
V = number of courses
E = number of prerequisite relation
"""

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in relations:
            graph[u - 1].append(v - 1)

        memo = [-1] * n

        def calculateTime(course):
            if memo[course] != -1:
                return memo[course]

            if not graph[course]:
                memo[course] = time[course]
                return memo[course]

            max_prerequisite_time = 0
            for prereq in graph[course]:
                max_prerequisite_time = max(max_prerequisite_time, calculateTime(prereq))

            memo[course] = max_prerequisite_time + time[course]
            return memo[course]

        overall_min_time = 0
        for course in range(n):
            overall_min_time = max(overall_min_time, calculateTime(course))
        
        return overall_min_time
