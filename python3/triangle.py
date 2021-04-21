"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = 10**10
        n = len(triangle)

        if n == 1:
            return triangle[0][0]

        for i in range(1, n):
            item = triangle[i]
            m = len(item)
            for j in range(m):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == m-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])

                if i == n-1:
                    ans = min(ans, triangle[i][j])

        return ans
