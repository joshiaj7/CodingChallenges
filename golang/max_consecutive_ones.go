package main

// Space	: O(1)
// Time		: O(n)

func findMaxConsecutiveOnes(nums []int) int {
	ans, count := 0, 0
	l := len(nums)

	for i := 0; i < l; i++ {
		if nums[i] == 0 {
			ans = Max(ans, count)
			count = 0
		} else {
			count++
		}
	}

	return Max(ans, count)
}
