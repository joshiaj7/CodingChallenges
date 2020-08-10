# leetcode

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            item1 = nums1
            item2 = nums2
        else:
            item1 = nums2
            item2 = nums1
        
        credit = {}
        
        for i in item2:
            if i in credit:
                credit[i] += 1
            else:
                credit[i] = 1
        
        ans = []
        
        for j in item1:
            if j in credit:
                if credit[j] > 0:
                    ans.append(j)
                    credit[j] -= 1
        
        
        return ans