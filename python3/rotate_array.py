# leetcode

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        leng = len(nums)
        k = k % leng
        
        pref_list = nums[-k:]
        pref = len(pref_list)
        suf_list = nums[:-k]
        suf = len(suf_list)
        
        # pref
        for idx in range(pref):
            nums[idx] = pref_list[idx]
            
        # suf
        for idx in range(suf):
            nums[idx+pref] = suf_list[idx]