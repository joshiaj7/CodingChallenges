# Space : O(n)
# Time  : O(n**2)


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hashmap = {}
        ans = 0
        
        for i in A:
            for j in B:
                if i + j not in hashmap:
                    hashmap[i+j] = 1
                else:
                    hashmap[i+j] += 1
        
        for k in C:
            for l in D:
                if -(k+l) in hashmap:
                    ans += hashmap[-(k+l)]
        
        return ans
        