"""
Space : O(n)
Time  : O(n log n)
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        target = n // 2
        d = {}
        
        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
                
        count = 0
        sc = sorted(list(d.values()), reverse=True)
        i = 0
        
        while count < target and i < n:
            count += sc[i]
            i += 1
        
        return i
        