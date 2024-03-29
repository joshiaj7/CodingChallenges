"""
Space   : O(1)
Time    : O(n * log(sum weights - max weights))
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) // 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > days: 
                left = mid + 1
            else: 
                right = mid
        return left
