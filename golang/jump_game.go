package main

/*
Space	: O(1)
Time	: O(n)
*/

func canJump(nums []int) bool {
	n := len(nums)
	if n == 1 {
		return true
	}

	i := 1
	credit := nums[0]
	for credit > 0 {
		credit = Max(credit-1, nums[i])
		if i == n-1 {
			return true
		}
		i++
	}

	return false
}
