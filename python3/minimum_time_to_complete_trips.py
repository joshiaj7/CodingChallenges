"""
Space   : O(1)
Time    : O(n log(k))
"""


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, totalTrips * min(time)

        while left <= right:
            mid = (left + right) // 2

            total = 0
            for t in time:
                total += mid // t

            if total < totalTrips:
                left = mid + 1
            else:
                right = mid - 1 

        return left
