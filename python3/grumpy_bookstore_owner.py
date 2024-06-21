from typing import List

"""
Space   : O(n)
Time    : O(n)
Sliding window
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        n = len(customers)
        window = []
        sumVal = 0

        maxVal = 0
        endIdx = 0

        # get highest grumpy with sliding window
        for i in range(n):
            if grumpy[i] == 1:
                window.append(customers[i])
                sumVal += customers[i]
            else:
                window.append(0)
                
            if len(window) > minutes:
                sumVal -= window[0]
                window = window[1:]

            if sumVal > maxVal:
                maxVal = sumVal
                endIdx = i

        startIdx = max(0, endIdx - minutes + 1)

        # calculate everything
        for i in range(n):
            if i >= startIdx and i <= endIdx:
                ans += customers[i]
            elif grumpy[i] == 0:
                ans += customers[i]

        return ans
        