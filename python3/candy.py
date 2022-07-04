"""
Space : O(n)
Time  : O(n)

Method:
Forward and backward iteration
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        
        c = [1 for _ in range(n)]
        
        # forward
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                c[i] = max(c[i], c[i-1] + 1) 
        
        # backward
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                c[i] = max(c[i], c[i+1] + 1) 
    
        return sum(c)
