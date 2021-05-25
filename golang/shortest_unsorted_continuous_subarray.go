package main

// Space   : O(1)
// Time    : O(n)

func findUnsortedSubarray(nums []int) int {
	n := len(nums)
	start, end := n-1, 0

	isAsc := true
	high := nums[0]
	for i := 1; i < n; i++ {
		if nums[i] < high {
			end = Max(end, i)
			isAsc = false
		}
		high = Max(high, nums[i])
	}

	if isAsc {
		return 0
	}

	low := nums[n-1]
	for j := n - 2; j >= 0; j-- {
		if nums[j] > low {
			start = Min(start, j)
		}
		low = Min(low, nums[j])
	}

	return end - start + 1
}
