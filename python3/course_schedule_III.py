import heapq

"""
Space : O(n)
Time  : O(n log n)

Method
heap
"""


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        time = 0

        for dur, last in courses:
            heapq.heappush(heap, -dur)
            time += dur
            if time > last:
                time += heapq.heappop(heap)

        return len(heap)
