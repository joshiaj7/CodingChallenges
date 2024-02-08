package main

/*
Space	: O(n)
Time	: O(n log n)
*/

func numSquares(n int) int {
	dp := make([]int, n+1)

	for i := 1; i <= n; i++ {
		dp[i] = 1000
	}

	for i := 0; i <= n; i++ {
		j := 0

		for i-j*j >= 0 {
			sq := j * j
			dp[i] = Min(dp[i], dp[i-sq]+1)
			j++
		}
	}

	return dp[n]
}
