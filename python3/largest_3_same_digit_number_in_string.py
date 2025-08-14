"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        n = len(num)

        curr = num[0]
        occur = 1
        for i in range(1, n):
            if num[i] == curr:
                occur += 1
            else:
                curr = num[i]
                occur = 1

            if occur >= 3:
                if ans == "" or (int(ans) < int(curr * 3)):
                    ans = curr * 3

        return ans
        