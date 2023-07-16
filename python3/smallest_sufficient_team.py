from typing import List

"""
Space   : O(2 ^ n)
Time    : O(m * 2 ^ n)
"""


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        dp = {0: []}

        skill_index = {}
        for i, skill in enumerate(req_skills):
            skill_index[skill] = i

        for i, person in enumerate(people):
            cur_skill = 0
            for skill in person:
                if skill in skill_index:
                    cur_skill |= 1 << skill_index[skill]

            temp_dp = dp.copy()
            for prev, need in dp.items():
                comb = prev | cur_skill
                if comb == prev:
                    continue
                if comb not in temp_dp or len(temp_dp[comb]) > len(need) + 1:
                    temp_dp[comb] = need + [i]

            dp = temp_dp

        return dp[(1 << n) - 1]
