"""
Space   : O(n)
Time    : O(n log n)

Method:
Sort the queue by the tallest first
Then insert each person by its index (p[1]) 
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
