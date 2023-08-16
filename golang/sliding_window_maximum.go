package main

/*
Space	: O(k)
Time	: O(n)
*/

func maxSlidingWindow(nums []int, k int) []int {
	window, ans := [][]int{}, []int{}
	n := len(nums)

	for i := 0; i < n; i++ {
		if len(window) > 0 && i-k >= window[0][1] {
			// popleft
			window = window[1:]
		}

		for len(window) > 0 && nums[i] > window[len(window)-1][0] {
			// popright
			window = window[:len(window)-1]
		}
		window = append(window, []int{nums[i], i})

		if i-k+1 >= 0 {
			ans = append(ans, window[0][0])
		}
	}

	return ans
}
