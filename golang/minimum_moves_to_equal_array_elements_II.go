package golang

// Space : O(1)
// Time  : O(n log n)

import (
	"sort"
)

func minMoves2(nums []int) int {
	median, ans, n := 0, 0, len(nums)
	sort.Ints(nums)

	if n%2 == 0 {
		median = (nums[n/2] + nums[(n/2)-1]) / 2
	} else {
		median = nums[n/2]
	}

	for i := 0; i < n; i++ {
		if nums[i] > median {
			ans += nums[i] - median
		} else {
			ans += median - nums[i]
		}
	}

	return ans
}
