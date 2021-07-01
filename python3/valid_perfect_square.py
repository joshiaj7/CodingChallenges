# Space : O(1)
# Time  : O(log n)

class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        i = 1

        while (i * i <= n):
            if i*i == n:
                return True
            i += 1

        return False
