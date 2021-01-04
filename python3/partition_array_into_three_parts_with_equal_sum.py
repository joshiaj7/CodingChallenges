"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        mean = sum(arr) / 3
        
        if mean % 1 > 0:
            return False
        
        mean = int(mean)
        
        count = 0
        subarr = 0
        for i in arr:
            count += i
            if count == mean:
                count = 0
                subarr += 1
            if subarr == 3:
                return True
        
        return False