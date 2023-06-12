package main

import "fmt"

/*
Space	: O(1)
Time	: O(n)
*/

func summaryRanges(nums []int) []string {
	n := len(nums)
	ans := []string{}

	if n == 0 {
		return ans
	}

	start := -1
	for i := 0; i < n; i++ {
		if start == -1 {
			start = nums[i]
			continue
		}

		if nums[i] != nums[i-1]+1 {
			if nums[i-1] == start {
				ans = append(ans, fmt.Sprintf("%d", start))
			} else {
				ans = append(ans, fmt.Sprintf("%d->%d", start, nums[i-1]))
			}
			start = nums[i]
		}
	}

	if nums[n-1] == start {
		ans = append(ans, fmt.Sprintf("%d", start))
	} else {
		ans = append(ans, fmt.Sprintf("%d->%d", start, nums[n-1]))
	}

	return ans
}
