class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        if len(intervals) == 0:
            return [newInterval]

        s, e = newInterval

        start, end = -1, -1
        for a, b in intervals:
            if b < s or a > e:
                continue
            if start == -1:
                start = min(s, a)
            end = max(b, e)

        if start == -1:
            start = s
        if end == -1:
            end = e

        inputted = False
        for a, b in intervals:
            if b < start or a > end:
                ans.append([a, b])
            elif (a >= start and a <= end) or (b >= start and b <= end):
                if not inputted:
                    ans.append([start, end])
                    inputted = True

        if not inputted:
            if end < ans[0][0]:
                ans.insert(0, [start, end])
            elif ans[-1][1] < start:
                ans.append([start, end])
            else:
                for idx in range(len(intervals)):
                    if end < ans[idx][0] and end > ans[idx-1][1]:
                        ans.insert(idx, [start, end])
                        break

        return ans
