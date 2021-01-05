"""
Space   : O(n)
Time    : O(wall layer * bricks)
"""


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall:
            return 0

        d = {}

        for x in wall:
            width = 0
            for i, b in enumerate(x):
                width += b
                if i < len(x)-1:
                    if width not in d:
                        d[width] = 1
                    else:
                        d[width] += 1

        ans = len(wall)
        for _, v in d.items():
            ans = min(len(wall) - v, ans)

        return ans
