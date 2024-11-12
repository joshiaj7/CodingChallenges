from collections import defaultdict
from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        ans = [] 
        
        items.sort(key=lambda x: (x[0], -x[1]))
        
        pairs = []
        currMax = 0
        for p, b in items:
            currMax = max(currMax, b)

            if not pairs:
                pairs.append((p, currMax))
            elif pairs[-1] != (p, currMax):
                pairs.append((p, currMax))

        ansMap = defaultdict(int)
        sortedQueries = sorted(queries)

        i = 0
        currMax = 0
        pairs.append([float('inf'), 0])
        for p in sortedQueries:
            if p < pairs[0][0]:
                ansMap[p] = 0
                continue
            
            while i < len(pairs)-1 and pairs[i][0] < p and pairs[i+1][0] <= p:
                i += 1

            currMax = max(currMax, pairs[i][1])
            ansMap[p] = currMax

            
        for q in queries:
            ans.append(ansMap[q])
        
        return ans
