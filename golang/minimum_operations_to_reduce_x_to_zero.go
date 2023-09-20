package main

// Space	: O(n)
// Time		: O(n)

func minOperations(nums []int, x int) int {
	longest := 0
	allSummInArray := 0
	for _, num := range nums {
		allSummInArray += num
	}

	if allSummInArray < x {
		return -1
	} else if allSummInArray == x {
		return len(nums)
	}

	sumTotal := 0
	left, right := 0, 0

	for left < len(nums) {
		sumTotal += nums[left]
		left++
		for sumTotal > allSummInArray-x {
			sumTotal -= nums[right]
			right++
		}

		if sumTotal == allSummInArray-x {
			longest = Max(longest, left-right+1)
		}
	}

	if longest == 0 {
		return -1
	}

	return len(nums) - longest + 1
}
