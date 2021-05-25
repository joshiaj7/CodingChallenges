package main

// Space : O(1)
// Time  : O(n)

func missingNumber(nums []int) int {
	totalNums, totalRange := 0, 0
	n := len(nums)

	for i := 0; i < n; i++ {
		totalNums += nums[i]
		totalRange += i + 1
	}

	return totalRange - totalNums
}
