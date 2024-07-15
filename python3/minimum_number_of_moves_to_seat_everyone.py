from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans = 0
        n = len(seats)

        seats.sort()
        students.sort()

        for i in range(n):
            ans += abs(students[i] - seats[i])

        return ans
