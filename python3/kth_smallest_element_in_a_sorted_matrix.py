from bisect import bisect_right

# Space : O(1)
# Time  : O(n log(A))


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        high, low = matrix[-1][-1], matrix[0][0]

        while low < high:
            cnt = 0
            mid = low + (high-low) // 2
            for i in range(row):
                cnt += bisect_right(matrix[i], mid)
            if cnt < k:
                low = mid+1
            else:
                high = mid

        return low
