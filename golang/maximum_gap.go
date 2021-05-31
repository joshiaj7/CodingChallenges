package main

import "sort"

func maximumGap(nums []int) int {
	ans, n := 0, len(nums)

	if n <= 1 {
		return 0
	}

	sort.Ints(nums)
	for i := 1; i < n; i++ {
		ans = Max(ans, nums[i]-nums[i-1])
	}

	return ans
}
