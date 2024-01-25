package main

/*
Space	: O(nm)
Time	: O(nm)
*/

func longestCommonSubsequence(text1 string, text2 string) int {
	l1 := len(text1)
	l2 := len(text2)
	dp := [][]int{}

	for i := 0; i <= l1; i++ {
		line := []int{}
		for j := 0; j <= l2; j++ {
			line = append(line, 0)
		}
		dp = append(dp, line)
	}

	for i := l1 - 1; i >= 0; i-- {
		for j := l2 - 1; j >= 0; j-- {
			if text1[i] == text2[j] {
				dp[i][j] = dp[i+1][j+1] + 1
			} else {
				dp[i][j] = Max(dp[i+1][j], dp[i][j+1])
			}
		}
	}

	return dp[0][0]
}
