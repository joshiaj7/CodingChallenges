"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist1, dist2 = 0, 0
        temp1, temp2 = 0, 0
        n = len(seats)

        for i in range(n):
            # forward
            if seats[i] == 0:
                temp1 += 1
                dist1 = max(dist1, temp1)
            else:
                temp1 = 0

            # backward
            if seats[n-1-i] == 0:
                temp2 += 1
                dist2 = max(dist2, temp2)
            else:
                temp2 = 0

        if dist1 % 2 == 1:
            mid = (dist1+1) // 2
        else:
            mid = (dist1) // 2

        return max(mid, temp1, temp2)
