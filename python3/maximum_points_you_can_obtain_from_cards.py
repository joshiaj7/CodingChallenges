# Space   : O(1)
# Time    : O(k)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ans = window = sum(cardPoints[:k])
        l, r = k-1, n-1

        while l >= 0:
            window += cardPoints[r] - cardPoints[l]
            ans = max(ans, window)
            l -= 1
            r -= 1

        return ans
