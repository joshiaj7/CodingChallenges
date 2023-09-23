from typing import List

"""
Space : O(n)
Time  : O(len(word) * max len(word[i]))

Mehtod:
DP - bottom up
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = 0
        dp = {}
        words.sort(key=lambda w: len(w))
        for word in words:
            for i in range(len(word)):
                mask = word[:i] + word[i+1:]
                dp[word] = max(dp.get(mask, 0) + 1, dp.get(word, 0))
                ans = max(ans, dp[word])

        return ans
