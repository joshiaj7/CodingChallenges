from typing import List

"""
Space   : O(1)
Time    : O(log n)

binary search
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1

        while left < right:
            mid = (left + right) // 2

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid

            if arr[mid - 1] < arr[mid] < arr[mid+1]:
                left = mid + 1

            if arr[mid - 1] > arr[mid] > arr[mid+1]:
                right = mid
            
        return 0
