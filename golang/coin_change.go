package main

import (
	"sort"
)

// Space   : O(amount + 1)
// Time    : O((amount + 1) * coins)
// DP approach

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	n := len(dp)
	sort.Ints(coins)

	for j := 1; j < n; j++ {
		dp[j] = 2147483647
	}

	for _, c := range coins {
		for i := 0; i < n; i++ {
			if i-c >= 0 {
				dp[i] = Min(dp[i-c]+1, dp[i])
			}
		}
	}

	if dp[n-1] == 2147483647 {
		return -1
	}
	return dp[n-1]
}
