from typing import Optional, List
from model import ListNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        p1, p2, p3 = head, head.next, head.next.next
        i2 = 1

        if not p3:
            return [-1, -1]

        ans = [float('inf'), -float('inf')]
        points = []
        while p3:
            if p2.val > p1.val and p2.val > p3.val:
                points.append(i2)
            elif p2.val < p1.val and p2.val < p3.val:
                points.append(i2)

            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
            i2 += 1

        if len(points) <= 1:
            return [-1, -1]

        for i in range(len(points)-1):
            ans[0] = min(ans[0], points[i+1] - points[i])

        ans[1] = max(ans[1], points[-1] - points[0])

        return ans
