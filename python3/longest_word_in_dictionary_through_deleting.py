"""
Space   : O(n)
Time    : O(n**2)
"""


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans = ""

        for word in d:
            a, b = len(word), len(ans)
            if a < b or (a == b and word > ans):
                continue

            i = 0
            for x in s:
                if x == word[i]:
                    i += 1
                if i == a:
                    ans = word
                    break

        return ans
