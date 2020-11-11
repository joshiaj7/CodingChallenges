"""
Space   : O(n)
Time    : O(n**2)
"""


class Solution:
    def getPythagoras(self, p1: List[int], p2: List[int]) -> float:
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**-2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pyths = set()
        points = [p1, p2, p3, p4]

        for i in range(4):
            for j in range(i+1, 4):
                if points[i] != points[j]:
                    pyths.add(self.getPythagoras(points[i], points[j]))
                else:
                    return False

        if len(pyths) == 2:
            return True

        return False
