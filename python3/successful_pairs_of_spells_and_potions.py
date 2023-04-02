"""
Space   : O(1)
Time    : O(m log m + n log m)
"""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        n, m =  len(spells), len(potions)
        potions = sorted(potions)

        for spell in spells:
            if spell * potions[0] >= success:
                ans.append(m)
                continue
            
            if spell * potions[-1] < success:
                ans.append(0)
                continue

            left, right = 0, m-1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] * spell < success:
                    left = mid + 1
                else:
                    right = mid - 1

            ans.append(m - left)

        return ans
