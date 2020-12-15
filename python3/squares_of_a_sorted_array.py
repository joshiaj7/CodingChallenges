"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp1, temp2, ans = [], [], []
        n = len(nums)
        
        i = 0  
        while i < n:
            if nums[i] < 0:
                temp1.insert(0, nums[i] ** 2)
            else:
                temp2.append(nums[i] ** 2)
            i += 1
        
        if not temp1:
            return temp2
        elif not temp2:
            return temp1
        
        x, y = 0, 0
        while x < len(temp1) and y < len(temp2):
            if temp1[x] < temp2[y]:
                ans.append(temp1[x])
                x += 1
            else:
                ans.append(temp2[y])
                y += 1
        
        if x == len(temp1):
            ans += temp2[y:]
        if y == len(temp2):
            ans += temp1[x:]
        
        return ans
