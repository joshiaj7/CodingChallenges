class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        ans = 0
        start = timeSeries[0]
        end = timeSeries[0] + duration
        
        for t in timeSeries[1:]:
            if t < end:
                end = t + duration
            else:
                ans += (end - start)
                start = t
                end = t + duration
              
        ans += (end - start)
        return ans

        
        