"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        greatest = max(candies)

        for x in candies:
            if x + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)

        return ans
