from bisect import bisect

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        mono = []

        for obs in obstacles:
            i = bisect(mono, obs)
            ans.append(i + 1)

            if i == len(mono):
                mono.append(obs)
            else:
                mono[i] = obs

        return ans
