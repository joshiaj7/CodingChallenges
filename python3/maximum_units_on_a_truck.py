# Space : O(1)
# Time  : O(n log n)

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        
        for num, size in boxTypes:
            if truckSize - num >= 0:
                truckSize -= num
                ans += num * size
            elif truckSize - num < 0:
                ans += truckSize * size
                truckSize = 0
            if truckSize == 0:
                break
            
        return ans