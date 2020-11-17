import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        Personal Attempt
        Space   : O(1)
        Time    : O(n)
        """

        # get Highest Common Factor
        # T = O(log(ab))
        g = math.gcd(p, q)

        h, w = p, q
        x, y = 0, 0

        while True:
            if x == w:
                mx = -g
            elif x == 0:
                mx = g

            if y == h:
                my = -g
            elif y == 0:
                my = g

            x += mx
            y += my

            if (x, y) == (q, 0):
                return 0
            if (x, y) == (q, p):
                return 1
            if (x, y) == (0, p):
                return 2

    def mirrorReflectionBest(self, p: int, q: int) -> int:
        """
        Best Solution
        Space   : O(1)
        Time    : O(log(pq))
        """
        g = math.gcd(p, q)
        m, n = q // g, p // g
        if n % 2 == 0:
            return 2

        return m % 2
