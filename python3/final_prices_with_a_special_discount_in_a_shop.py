from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []

        for i in range(n):
            disc = 0
            j = i+1

            while j < n and prices[j] > prices[i]:
                j += 1

            if j < n:
                disc = prices[j]

            ans.append(prices[i] - disc)

        return ans
        