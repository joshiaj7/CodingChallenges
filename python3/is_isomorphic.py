"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}

        for idx in range(len(s)):
            if s[idx] not in s_map:
                s_map[s[idx]] = t[idx]
                if t[idx] in t_map:
                    if t_map[t[idx]] != s[idx]:
                        return False
                else:
                    t_map[t[idx]] = s[idx]
            else:
                if s_map[s[idx]] != t[idx]:
                    return False

        return True
