"""
Space   : O(1)
Time    : O(1)
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 1 min = 6 degrees
        m_angle = minutes * 6
        
        # 1 hour = 30 degress
        hour = 0 if hour == 12 else hour
        h_angle = (hour * 30) + (minutes / 2)
        
        ans = abs(min(abs(m_angle - h_angle), (360 - abs(m_angle - h_angle))))
        return ans