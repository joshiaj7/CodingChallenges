"""
Space   : O(n)
Time    : O(nk)
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0

        word = ""
        for c in s:
            word += str(ord(c) - ord('a') + 1)

        while k > 0:
            temp = 0
            for c in word:
                temp += int(c)
            
            k -= 1
            if k == 0:
                ans = temp
                break

            word = str(temp)

        return ans
        