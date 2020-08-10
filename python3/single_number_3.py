# leetcode

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                
        for key, val in hashmap.items():
            if val == 1:
                res.append(key)
        
        return res