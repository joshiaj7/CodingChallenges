package main

/*
Space	: O(n)
Time	: O(n**2)
*/

func findNumberOfLIS(nums []int) int {
	n := len(nums)
	if n <= 1 {
		return n
	}

	lengths, counts := []int{}, []int{}
	for i := 0; i < n; i++ {
		lengths = append(lengths, 0)
		counts = append(counts, 1)
	}

	for j := 0; j < n; j++ {
		for i := 0; i < j; i++ {
			if nums[i] < nums[j] {
				if lengths[i] >= lengths[j] {
					lengths[j] = lengths[i] + 1
					counts[j] = counts[i]
				} else if lengths[j] == lengths[i]+1 {
					counts[j] += counts[i]
				}
			}
		}
	}

	longest, ans := 0, 0
	for _, v := range lengths {
		longest = Max(longest, v)
	}

	for i, v := range counts {
		if lengths[i] == longest {
			ans += v
		}
	}

	return ans
}
