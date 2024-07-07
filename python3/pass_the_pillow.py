"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ans = 0

        halfCourse = (n - 1)
        fullCourse = halfCourse * 2
        time %= fullCourse

        if time > halfCourse:
            time %= halfCourse
            return n - time

        return time + 1
        