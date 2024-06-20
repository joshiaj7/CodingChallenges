from typing import List

"""
Space   : O(1)
Time    : O(n log n + m log n)
"""

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans = -1
        l = 1
        r = (position[-1] - position[0])

        while l <= r:
            mid = l + (r - l) // 2
            last_position, balls = position[0], 1

            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    last_position = position[i]
                    balls += 1

            if balls >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
