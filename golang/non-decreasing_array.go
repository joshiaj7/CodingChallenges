package golang

// Space   : O(1)
// Time    : O(n)

func checkPossibility(nums []int) bool {
	n := len(nums)
	if n == 1 {
		return true
	}

	forward, backward := 0, 0
	fmax, bmin := nums[0], nums[n-1]

	for i := 1; i < n; i++ {
		if fmax > nums[i] {
			forward++
		}
		fmax = Max(fmax, nums[i])
	}

	for j := n - 2; j >= 0; j-- {
		if bmin < nums[j] {
			backward++
		}
		bmin = Min(bmin, nums[j])
	}

	return Min(forward, backward) <= 1
}
