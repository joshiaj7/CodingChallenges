package golang

// Space	: O(n)
// Time		: O(n)

func max(a int, b int) int {
    if a < b {
        return b
    } 
    return a
}

func rob2(nums []int) int {
    res1, res2 := 0, 0
    n := len(nums)
    dp1 := make([]int, n-1)
    dp2 := make([]int, n-1)
    
    if n == 0 {
        return 0
    } else if n == 1 {
        return nums[0]
    }
    
    for i := 0; i < n - 1; i++ {
        if i <= 1 {
            dp1[i] = nums[i]
            dp2[i] = nums[i+1]
        } else if i == 2 {
            dp1[i] = nums[i] + dp1[i-2]
            dp2[i] = nums[i+1] + dp2[i-2]
        } else { 
            dp1[i] = max(nums[i] + dp1[i-2], nums[i] + dp1[i-3])
            dp2[i] = max(nums[i+1] + dp2[i-2], nums[i+1] + dp2[i-3])
        }
        res1 = max(dp1[i], res1)
        res2 = max(dp2[i], res2)
        
    }
    
    return max(res1, res2)
    
}