package main

// Space   : O(1)
// Time    : O(n)

func findErrorNums(nums []int) []int {
	n := len(nums)
	dict := make(map[int]int)
	totalVal, totalIdx, totalUnique := 0, 0, 0

	for i := 0; i < n; i++ {
		if _, ok := dict[nums[i]]; !ok {
			dict[nums[i]] = 1
		}
		totalVal += nums[i]
		totalIdx += i + 1
	}

	for k := range dict {
		totalUnique += k
	}

	return []int{totalVal - totalUnique, totalIdx - totalUnique}
}
