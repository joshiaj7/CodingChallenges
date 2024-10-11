from typing import List
from heapq import heapify, heappop, heappush

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        order = sorted(range(len(times)), key=lambda k: times[k][0])
        chairs = [i for i in range(len(times))]
        seats = []

        heapify(chairs)
        heapify(seats)

        for i in order:
            arr, dep = times[i]
        
            while seats and seats[0][0] <= arr:
                heappush(chairs, heappop(seats)[1])
            chair = heappop(chairs)

            if i == targetFriend: 
                return chair

            heappush(seats, (dep, chair))


        return -1
        