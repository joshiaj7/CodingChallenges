package main

// Space : O(n)
// Time  : O(n**2)

func jump(nums []int) int {
	n := len(nums)
	dp := []int{}
	dp = append(dp, 0)

	if n < 2 {
		return 0
	}

	for x := 1; x < n; x++ {
		dp = append(dp, 10000)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < nums[i]; j++ {
			dp[i+j+1] = Min(dp[j+i+1], dp[i]+1)
			if j+i+1 == n-1 {
				return dp[n-1]
			}
		}
	}

	return dp[n-1]
}
