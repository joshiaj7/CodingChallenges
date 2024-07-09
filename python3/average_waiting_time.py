from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        n = len(customers)

        curr = customers[0][0]
        for a, b in customers:
            if curr < a:
                curr = a
            
            curr += b
            time += (curr - a)

        return time / n
