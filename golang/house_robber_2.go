package golang

// Space	: O(n)
// Time		: O(n)

func rob2(nums []int) int {
	res1, res2 := 0, 0
	n := len(nums)
	dp1 := make([]int, n-1)
	dp2 := make([]int, n-1)

	if n == 0 {
		return 0
	} else if n == 1 {
		return nums[0]
	}

	for i := 0; i < n-1; i++ {
		if i <= 1 {
			dp1[i] = nums[i]
			dp2[i] = nums[i+1]
		} else if i == 2 {
			dp1[i] = nums[i] + dp1[i-2]
			dp2[i] = nums[i+1] + dp2[i-2]
		} else {
			dp1[i] = Max(nums[i]+dp1[i-2], nums[i]+dp1[i-3])
			dp2[i] = Max(nums[i+1]+dp2[i-2], nums[i+1]+dp2[i-3])
		}
		res1 = Max(dp1[i], res1)
		res2 = Max(dp2[i], res2)

	}

	return Max(res1, res2)

}
