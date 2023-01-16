from bisect import bisect_right

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        overlap = False
        ns, ne = newInterval
        
        cs, ce = -1, -1
        for s, e in intervals:
            if s <= ns <= e or e <= ne <= e or ns <= s <= ne or ns <= e <= ne:
                overlap = True
                if cs == -1:
                    cs = min(s, ns)
                    ce = max(e, ne)
                    continue

                cs = min(s, ns, cs)
                ce = max(e, ne, ce)

        if not overlap:
            i = bisect_right(intervals, newInterval)
            intervals.insert(i, newInterval)
            return intervals

        skip = False
        for s, e in intervals:
            if s <= ns <= e or e <= ne <= e or ns <= s <= ne or ns <= e <= ne: 
                skip = True
                continue
            elif skip:
                skip = False
                ans.append([cs, ce])
            ans.append([s, e])

        if skip:
            ans.append([cs, ce])

        return ans



