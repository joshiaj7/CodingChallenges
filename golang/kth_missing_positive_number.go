package main

// Space	: O(1)
// Time		: O(maxNum)

func findKthPositive(arr []int, k int) int {
	n := len(arr)
	maxNum := arr[n-1]

	idx := 0
	for i := 1; i <= maxNum; i++ {
		if i == arr[idx] {
			idx++
		} else {
			k--
		}

		if k == 0 {
			return i
		}
	}

	return maxNum + k
}
