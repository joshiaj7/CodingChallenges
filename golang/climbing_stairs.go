package main

func climbStairs(n int) int {
	dp := []int{1, 1, 2}

	if n < 3 {
		return dp[n]
	}

	for i := 3; i <= n; i++ {
		dp = append(dp, dp[i-1]+dp[i-2])
	}

	return dp[n]
}
