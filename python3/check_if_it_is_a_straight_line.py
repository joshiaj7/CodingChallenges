from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        coordinates = sorted(coordinates)

        dx_rate = coordinates[0][0] - coordinates[1][0]
        dy_rate = coordinates[0][1] - coordinates[1][1]

        for i in range(n - 1):
            d_x = coordinates[i][0] - coordinates[i + 1][0]
            d_y = coordinates[i][1] - coordinates[i + 1][1]
            if not (d_x * dy_rate == dx_rate * d_y):
                return False

        return True
