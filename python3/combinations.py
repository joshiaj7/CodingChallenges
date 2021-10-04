from itertools import combinations

# Space     : O(n^2)
# Time      : O(n!)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]
        res = []
        
        comb = combinations(arr, k)
        for c in comb:
            res.append(list(c))
        
        return res
