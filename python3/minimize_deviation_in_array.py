from heapq import heappop, heappush, heapify

"""
Space   : O(n)
Time    : O(n (log n) (log m))
n == len(nums)
m == max(nums)
"""


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = nums[i] * -2
            else:
                nums[i] *= -1

        heap = list(set(nums))
        heapify(heap) 

        ma, mi = heap[0], max(heap) 
        ans = ma - mi

        while ma % 2 == 0:
            x = ma // 2
            heappop(heap)
            heappush(heap, x)
            ma, mi = heap[0], max(mi, x)
            ans = max(ans, ma - mi)

        return -ans
