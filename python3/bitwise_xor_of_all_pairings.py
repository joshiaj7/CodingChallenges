class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n = len(nums1)
        m = len(nums2)
        d = {}
        
        for x in nums1:
            if x in d:
                d[x] += m
            else:
                d[x] = m

        for x in nums2:
            if x in d:
                d[x] += n
            else:
                d[x] = n

        for k, v in d.items():
            if v % 2 == 1:
                ans ^= k

        return ans
