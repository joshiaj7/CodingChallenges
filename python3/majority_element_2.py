class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []

        if len(nums) == 0:
            return ans

        hashmap = {}
        N = len(nums)

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        for k, v in hashmap.items():
            if v > int(N/3):
                ans.append(k)

        return ans
