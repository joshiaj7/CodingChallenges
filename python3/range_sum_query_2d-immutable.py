# Space : O(row*col)
# Time  : O(row*col)

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums.copy()

    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        for idx in range(i, j+1):
            ans += self.arr[idx]
            
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)