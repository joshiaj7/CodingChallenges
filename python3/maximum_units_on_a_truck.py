"""
Space : O(1)
Time  : O(n log n)
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        cap = 0
        boxTypes.sort(key=lambda b: -b[1])
        
        for q, v in boxTypes:
            if q + cap <= truckSize:
                cap += q
                ans += (q * v)
            else:
                space = truckSize - cap
                cap += space
                ans += space * v
            if cap == truckSize:
                break 
        
        return ans
