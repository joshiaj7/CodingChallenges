package main

// Space : O(n)
// Time  : O(n)

func minCostClimbingStairs(cost []int) int {
    n := len(cost)
    var dp []int
    
    for i := 0; i < n; i++ {
        dp = append(dp, 0)
    }
    
    for i := 0; i < n; i++ {
        if i < 2 {
            dp[i] = cost[i]
        } else {
            dp[i] = cost[i] + Min(dp[i-2], dp[i-1])
        }
    }
    
    return Min(dp[n-2], dp[n-1])
}