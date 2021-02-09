"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        
        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
                
        for k in d.keys():
            if k == 0:
                if d[0] > 1:
                    return True
            elif k * 2 in d:
                return True
            
        return False