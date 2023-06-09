from typing import List

"""
Space   : O(1)
Time    : O(log n)
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n-1

        while left <= right:
            if letters[left] > target:
                return letters[left]

            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid


        if letters[-1] > target:
            return letters[-1]

        return letters[0]
