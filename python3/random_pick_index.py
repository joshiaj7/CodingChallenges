import random

# Space : O(n)
# Time  : O(n)


class Solution:

    def __init__(self, nums: List[int]):
        self.d = {}
        for i, x in enumerate(nums):
            if x not in self.d:
                self.d[x] = [i]
            else:
                self.d[x].append(i)

    def pick(self, target: int) -> int:
        l = len(self.d[target])
        return self.d[target][(random.randint(0, l-1))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
