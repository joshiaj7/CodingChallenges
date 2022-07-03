package main

func wiggleMaxLength(nums []int) int {
	n := len(nums)
	if n == 1 {
		return 1
	}

	var disc []int
	for i := 1; i < n; i++ {
		disc = append(disc, nums[i]-nums[i-1])
	}

	ans, last := 0, 0
	for i := 0; i < len(disc); i++ {
		if (last > 0 && disc[i] > 0) || (last < 0 && disc[i] < 0) || (disc[i] == 0) {
			continue
		}

		ans++
		last = disc[i]
	}

	return ans + 1
}
