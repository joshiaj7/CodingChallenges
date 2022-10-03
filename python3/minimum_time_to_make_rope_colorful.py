"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        n = len(colors)

        cur = colors[0]
        sum_time = neededTime[0]
        max_time = neededTime[0]
        for i in range(1, n):
            if colors[i] == cur:
                sum_time += neededTime[i]
                max_time = max(max_time, neededTime[i])
            else:
                # resolve prev color
                if sum_time > max_time:
                    ans += sum_time - max_time
                cur = colors[i]
                sum_time = neededTime[i]
                max_time = neededTime[i]

        if sum_time > max_time:
            ans += sum_time - max_time

        return ans
