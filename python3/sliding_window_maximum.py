from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Personal Attempt
        Space   : O(n)
        Time    : O(n**2)
        """
        if not nums:
            return []

        ans = []
        n = len(nums)
        dq = []

        for i in range(n):
            # check if expired
            if dq and dq[0][1] <= i - k:
                dq.pop(0)

            # utmost left in dq is the max val
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            dq.append([nums[i], i])

            # start fill ans i is fulfilled
            if i >= k - 1:
                ans.append(dq[0][0])

            # print(dq)

        return ans

    def maxSlidingWindowBest(self, nums: List[int], k: int) -> List[int]:
        """
        Best solution
        Space   : O(k)
        Time    : O(n)
        """

        window = deque()

        res = []

        for i in range(len(nums)):
            if window and i - k >= window[0][1]:
                window.popleft()

            while window and nums[i] > window[-1][0]:
                window.pop()
            window.append((nums[i], i))

            if i >= k - 1:
                res.append(window[0][0])

        return res


# LINE JAPAN
def solution(window_size, numbers):
    """
    Solution description.

    Time Complexity: O(n)
    Space Complexity: O(window_size)
    """

    d = deque()
    ans = []
    n = len(numbers)

    if window_size >= n:
        return [max(numbers)]

    for i, v in enumerate(numbers):
        while d and d[0] <= i - window_size:
            d.popleft()
        while d and v >= numbers[d[-1]]:
            d.pop()

        d.append(i)

        if i >= window_size - 1:
            ans.append(numbers[d[0]])

    return ans
