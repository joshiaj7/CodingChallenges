"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        n = len(answerKey)

        count_T, count_F = 0, 0
        left = 0
        for right in range(n):
            if answerKey[right] == "T":
                count_T += 1
            else:
                count_F += 1

            while min(count_T, count_F) > k:
                if answerKey[left] == "T":
                    count_T -= 1
                else:
                    count_F -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
