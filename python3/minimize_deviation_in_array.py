import heapq

"""
Best solution
Space   : O(n)
Time    : O(n (log n) (log m))
where n is number of nums and m = max(nums)
"""


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = list(set(-(x * 2 if x & 1 else x) for x in nums))
        heapq.heapify(heap)
        ma, mi = heap[0], max(heap)
        ans = ma - mi
        while ma % 2 == 0:
            x = ma // 2
            heapq.heapreplace(heap, x)
            ma, mi = heap[0], max(mi, x)
            ans = max(ans, ma - mi)
        return -ans
