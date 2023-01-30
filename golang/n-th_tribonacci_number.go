package main

func tribonacci(n int) int {
	dp := []int{0, 1, 1}

	if n < 3 {
		return dp[n]
	}

	for i := 3; i <= n; i++ {
		l := len(dp)
		dp = append(dp, dp[l-1]+dp[l-2]+dp[l-3])
	}

	return dp[n]
}
