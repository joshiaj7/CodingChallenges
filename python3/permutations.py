from itertools import permutations

# Space     : O(n^2)
# Time      : O(n!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = permutations(nums)
        
        for p in perm:
            res.append(list(p))
        
        return res
