"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans, indices = [], []
        n = len(s)

        for i in range(n):
            if s[i] == c:
                indices.append(i)

        start, end = -1, indices.pop(0)

        for i in range(n):
            if start >= 0 and end >= 0:
                ans.append(min(i - start, end - i))
            elif start == -1:
                ans.append(end - i)
            elif end == -1:
                ans.append(i - start)

            if i == end:
                start = end
                if not indices:
                    end = -1
                else:
                    end = indices.pop(0)

        return ans
