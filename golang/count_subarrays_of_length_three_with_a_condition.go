package main

func countSubarrays(nums []int) int {
	ans := 0
	n := len(nums)

	for i := range n - 2 {
		if 2*(nums[i]+nums[i+2]) == nums[i+1] {
			ans++
		}
	}

	return ans
}
