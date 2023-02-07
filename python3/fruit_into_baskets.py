"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        d = {}

        i = 0
        for j, f in enumerate(fruits):
            if f in d:
                d[f] += 1
            else:
                d[f] = 1

            while len(d) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i += 1

            ans = max(ans, j - i + 1)


        return ans

