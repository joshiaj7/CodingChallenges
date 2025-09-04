class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        one = abs(x - z)
        two = abs(y - z)

        if one < two:
            return 1
        elif one > two:
            return 2
        return 0
        