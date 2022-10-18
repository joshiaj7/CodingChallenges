"""
Space   : O(n)
Time    : O(nm)
m = len(memo[n-1])
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        memo = ["1"]

        def helper(s):
            n = len(s)
            word = ""

            for i in range(n):
                if i == 0:
                    cur = [s[i], 1]
                    continue

                if s[i] == cur[0]:
                    cur[1] += 1
                else:
                    word += "{}{}".format(cur[1], cur[0])
                    cur = [s[i], 1]

            word += "{}{}".format(cur[1], cur[0])

            return word

        for i in range(1, n):
            memo.append(helper(memo[i-1]))

        return memo[-1]
