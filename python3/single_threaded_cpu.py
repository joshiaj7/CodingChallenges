from heapq import heappush, heappop

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        heap = []
        n = len(tasks)
        
        # append index
        for i in range(n):
            tasks[i].append(i)

        tasks.sort(key=lambda x: (x[0], x[1], x[2]))

        complete = tasks[0][0]
        i = 0
        while len(ans) < len(tasks):
            while (i < len(tasks)) and (tasks[i][0] <= complete):
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if heap:
                t_diff, original_index = heappop(heap)
                complete += t_diff
                ans.append(original_index)
            elif i < len(tasks):
                complete = tasks[i][0]


        return ans
