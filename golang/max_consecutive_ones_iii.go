package main

// Space : O(n)
// Time  : O(n)

func longestOnes(nums []int, k int) int {
    ones, zeros, start, ans := 0, 0, 0, 0
    n := len(nums)
    
    for i := 0; i < n; i++ {
        if nums[i] == 1 {
            ones++
        } else {
            zeros++
        }
        
        for zeros > k {
            if nums[start] == 1 {
                ones--
            } else {
                zeros--
            }
            start++
        }
        
        ans = Max(ans, i-start+1)
    }
    
    return ans
}
