package main

// Space	: O(100)
// Time		: O(queryRow ^ 2)

func champagneTower(poured int, query_row int, query_glass int) float64 {
	dp := []float64{}
	for i := 0; i < 100; i++ {
		dp = append(dp, float64(0.0))
	}
	dp[0] = float64(poured)

	for i := 1; i < query_row+1; i++ {
		for j := i - 1; j >= 0; j-- {
			remain := (Max(dp[j], 1.0) - 1.0) / 2.0
			dp[j+1] += remain
			dp[j] = remain
		}
	}

	if dp[query_glass] >= 1 {
		return 1.0
	}
	return dp[query_glass]
}
