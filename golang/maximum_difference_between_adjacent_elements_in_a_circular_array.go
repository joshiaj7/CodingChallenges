package main

// Space	: O(1)
// Time		: O(n)

func maxAdjacentDistance(nums []int) int {
	ans := 0
	n := len(nums)

	for i := range n - 1 {
		subs := nums[i] - nums[i+1]
		if subs < 0 {
			subs *= -1
		}

		ans = Max(ans, subs)
	}

	subs := nums[0] - nums[n-1]
	if subs < 0 {
		subs *= -1
	}
	ans = Max(ans, subs)

	return ans
}
