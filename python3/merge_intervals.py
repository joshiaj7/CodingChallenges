"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])

        stack = []
        for item in intervals:
            if len(stack) == 0 or stack[-1][1] < item[0]:
                stack.append(item)
            else:
                stack[-1][1] = max(stack[-1][1], item[1])

        return stack
