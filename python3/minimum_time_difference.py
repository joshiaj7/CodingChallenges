from typing import List

"""
Space    : O(n)
Time     : O(n log n)
"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = float('inf')
        arr = []

        for time in timePoints:
            hour, minute = time.split(":")
            val = int(hour) * 60 + int(minute)
            arr.append(val)

        arr.sort()
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i-1])

        ans = min(ans, (arr[0] + 24*60) - arr[-1])

        return ans
        