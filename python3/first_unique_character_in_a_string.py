"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        index_map, count_map = {}, {}

        for i, c in enumerate(s):
            index_map[c] = i
            if c not in count_map:
                count_map[c] = 1
            else:
                count_map[c] += 1

        for k, v in index_map.items():
            if count_map[k] == 1:
                ans = min(ans, v)

        return ans if ans != len(s) else -1
