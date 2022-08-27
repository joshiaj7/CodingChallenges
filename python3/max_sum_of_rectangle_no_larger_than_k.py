from bisect import insort, bisect_left

"""
Space   : O(n^2)
Time    : O(m^2 * n * log(n))
"""


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSumSubarray(arr):
            sub_s_max = float('-inf')
            s_curr = 0
            prefix_sums = [float('inf')]
            for x in arr:
                insort(prefix_sums, s_curr)
                s_curr += x
                i = bisect_left(prefix_sums, s_curr - k)
                sub_s_max = max(sub_s_max, s_curr - prefix_sums[i])
            return sub_s_max

        m, n = len(matrix), len(matrix[0])

        # cumulative count
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]

        res = float('-inf')
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = []
                for x in range(m):
                    if y1 > 0:
                        arr.append(matrix[x][y2] - matrix[x][y1-1])
                    else:
                        arr.append(matrix[x][y2])
                res = max(res, maxSumSubarray(arr))

        return res
