package main

// # Space   : O(1)
// # Time    : O(log n)

func searchRange(nums []int, target int) []int {
	ans := []int{-1, -1}
	if len(nums) == 0 {
		return ans
	}

	s, m, e := 0, 0, len(nums)-1
	for s < e {
		m = (s + e) / 2
		if nums[m] < target {
			s = m + 1
		} else {
			e = m
		}
	}

	if nums[e] != target {
		return ans
	}
	ans[0] = e

	e = len(nums) - 1
	for s < e {
		m = ((s + e) / 2) + 1
		if nums[m] <= target {
			s = m
		} else {
			e = m - 1
		}
	}

	ans[1] = e
	return ans
}
