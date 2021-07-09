package main

// Space : O(1)
// Time  : O(n)

func findLengthOfLCIS(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    s, ans := 0, 1
    
    for i := 1; i < n; i++ {
        if nums[i] > nums[i-1] {
            ans = Max(ans, i-s+1)
        } else {
            s = i
        }
    }
    
    return ans
}