from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []

        ball_color = {}
        color_set = {}

        for x, y in queries:
            if x in ball_color:
                curr = ball_color[x]
                
                if color_set[curr] == 1:
                    del color_set[curr]
                else:
                    color_set[curr] -= 1

            ball_color[x] = y

            if y not in color_set:
                color_set[y] = 1
            else:
                color_set[y] += 1

            ans.append(len(color_set))

        return ans
