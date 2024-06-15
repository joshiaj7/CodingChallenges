from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, v in enumerate(temperatures): 
            while stack and temperatures[stack[-1]] < v:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)
                
        return ans
