"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = [i+1 for i in range(n)]
        
        i = 0
        while n > 1:
            i = (i + k - 1) % n
            people = people[:i] + people[i+1:]
            n -= 1

        return people[0]
        