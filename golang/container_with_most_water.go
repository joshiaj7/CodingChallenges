package main

// Space	: O(1)
// Time		: O(n)

func maxArea(height []int) int {
	ans := 0
	a, b := 0, len(height)-1

	for a < b {
		ans = Max(ans, (b-a)*Min(height[a], height[b]))
		if height[a] < height[b] {
			a++
		} else {
			b--
		}
	}

	return ans
}
