"""
Space : O(n)
Time  : O(n log n)
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        d = {}
        n = len(changed)
        
        if n % 2 == 1:
            return []
        
        for x in changed:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        
        changed.sort()
        for x in changed:
            if x in d and d[x] > 0:  
                if x*2 in d  and d[x*2] > 0:
                    d[x] -= 1
                    d[x*2] -= 1
                    ans.append(x)
                else:
                    return []
        
        return ans
