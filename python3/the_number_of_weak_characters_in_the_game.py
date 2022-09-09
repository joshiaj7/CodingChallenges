"""
Space : O(1)
Time  : O(n log n)
"""

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ans = 0
        n = len(properties)
        
        properties.sort(key=lambda x: (-x[0], x[1]))

        max_def = 0
        for _, d in properties:    
            if d < max_def:
                ans += 1
            else:
                max_def = d
        
        return ans
