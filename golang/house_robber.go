package main

// Space   : O(n)
// Time    : O(n)

func rob1(nums []int) int {
	ans := 0
	leng := len(nums)
	dp := make([]int, leng)

	for i, v := range nums {
		if i == 0 || i == 1 {
			dp[i] = v
		} else if i == 2 {
			dp[i] = v + dp[i-2]
		} else {
			if dp[i-2] > dp[i-3] {
				dp[i] = v + dp[i-2]
			} else {
				dp[i] = v + dp[i-3]
			}
		}

		if ans < dp[i] {
			ans = dp[i]
		}

	}

	return ans
}
