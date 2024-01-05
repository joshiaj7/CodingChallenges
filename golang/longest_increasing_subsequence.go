package main

/*
Space	: O(n)
Time	: O(n log n)
*/

func lengthOfLIS(nums []int) int {
	subsequence := []int{}

	for _, x := range nums {
		idx := BisectLeft(subsequence, x)
		if idx == len(subsequence) {
			subsequence = append(subsequence, x)
		} else {
			subsequence[idx] = x
		}
	}

	return len(subsequence)
}
