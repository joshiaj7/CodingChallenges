package main

/*
Space	: O(mn)
Time	: O(mn)
*/

func uniquePaths(m int, n int) int {
	var dp [][]int

	for i := 0; i < m; i++ {
		var temp []int
		for j := 0; j < n; j++ {
			temp = append(temp, 0)
		}
		dp = append(dp, temp)
	}

	for y := 0; y < m; y++ {
		for x := 0; x < n; x++ {
			if y == 0 && x == 0 {
				dp[y][x] = 1
			} else if y == 0 {
				dp[y][x] = dp[y][x-1]
			} else if x == 0 {
				dp[y][x] = dp[y-1][x]
			} else {
				dp[y][x] = dp[y][x-1] + dp[y-1][x]
			}
		}
	}

	return dp[m-1][n-1]
}
