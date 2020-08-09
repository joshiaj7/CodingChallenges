# leetcode
class Solution:
    def twoSum(self, nums: Lint[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        
        sorted_nums = sorted(nums)
    
        while start <= end:
            if sorted_nums[start] + sorted_nums[end] > target:
                end -= 1
            elif sorted_nums[start] + sorted_nums[end] < target:
                start += 1
            else:
                break
        
        item1 = sorted_nums[start]
        item2 = sorted_nums[end]
        
        ans = []
        
        for i in range(len(nums)):
            if nums[i] == item1 or nums[i] == item2:
                ans.append(i)

        print(ans)
        
        return ans