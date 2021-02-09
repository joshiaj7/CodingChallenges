"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        h1, h2 = {}, {}

        for i in range(len(list1)):
            h1[list1[i]] = i

        for j in range(len(list2)):
            h2[list2[j]] = j

        min_idx = 10**10
        ans = []
        intercept = {}

        for k, v in h1.items():
            if k in h2:
                intercept[k] = v + h2[k]
                min_idx = min(min_idx, intercept[k])

        for key, val in intercept.items():
            if val == min_idx:
                ans.append(key)

        return ans
