# leetcode

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        sort_val = []
        ans = []
        
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                

        for j in sorted(hashmap, key=hashmap.get, reverse=True):
            sort_val.append((j, hashmap[j]))
        
        
        for x, y in sort_val[:k]:
            ans.append(x)

        return ans