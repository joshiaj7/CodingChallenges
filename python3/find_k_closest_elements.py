import bisect

# Space : O(1)
# Time  : O(logn + k)


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        left = bisect.bisect_left(arr, x)-1
        right = left + 1

        while right-left-1 < k:
            if left == -1:
                right += 1
                continue

            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left+1:right]
