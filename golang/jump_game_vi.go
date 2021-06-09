package main

// Optimized dp-queue approach
// Space : O(n)
// Time  : O(n)


func maxResult(nums []int, k int) int {
    n := len(nums)
    var dp, q []int
    for i := 0; i < n; i++ {
        dp = append(dp, 0)
    }
    dp[0] = nums[0]
    q = append(q, 0)
    
    for j := 1; j < n; j++ {
        if q[0] < j-k {
            q = q[1:]
        }
        dp[j] = nums[j] + dp[q[0]]
        for len(q) > 0 && dp[q[len(q)-1]] <= dp[j] {
            q = q[:len(q)-1]
        }
        q = append(q, j)
    }
    
    return dp[n-1]
}