# Time  : O(n log n)
# Space : O(1)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hashmap = {}
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1

        prev = None
        take = leave = 0

        for x in sorted(hashmap.keys()):
            if prev != x-1:
                take, leave = hashmap[x] * x + \
                    max(take, leave), max(take, leave)
            else:
                take, leave = hashmap[x] * x + leave, max(take, leave)
            prev = x

        return max(take, leave)
