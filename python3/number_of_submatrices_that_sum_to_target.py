from collections import defaultdict

"""
Space   : O(mnn)
Time    : O(mnn)

method:
prefix sum
"""


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0

        for line in matrix:
            for i in range(1, n):
                line[i] += line[i-1]

        for col_start in range(n):
            for col_end in range(col_start, n):
                count = defaultdict(int)
                cur = 0
                count[0] = 1  # default for empty subarray
                for row in range(m):
                    cur += matrix[row][col_end] - \
                        (matrix[row][col_start-1] if col_start > 0 else 0)
                    ans += count[cur - target]
                    count[cur] += 1

        return ans
