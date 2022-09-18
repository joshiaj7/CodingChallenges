"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right = [0] * n, [0] * n
        ans = 0

        for i in range(n):
            left = i
            right = n - i - 1
            if i == 0:
                max_left[left] = height[left]
                max_right[right] = height[right]
            else:
                max_left[left] = max(height[left], max_left[left-1])
                max_right[right] = max(height[right], max_right[right+1])

        for i in range(n):
            max_level = min(max_left[i], max_right[i])
            if height[i] < max_level:
                ans += max_level - height[i]

        return ans
