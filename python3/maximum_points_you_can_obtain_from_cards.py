# Space   : O(1)
# Time    : O(k)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ans = total = sum(cardPoints[:k])
        
        for i in range(k-1, -1, -1):
            total += cardPoints[n-k+i] - cardPoints[i]
            ans = max(ans, total)
        
        return ans
        