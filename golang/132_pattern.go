package golang

// Space : O(n)
// Time	: O(n**2)

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func find132pattern(nums []int) bool {
	n := len(nums)

	if n < 3 {
		return false
	}

	var n1, n2 int

	for i := 0; i < n-2; i++ {
		n1 = nums[i]
		n2 = 1000000001

		var j int
		for j = n - 1; j > i; j-- {
			if nums[j] > n1 {
				if n2 == 1000000001 {
					n2 = nums[j]
					continue
				} else if nums[j] < n2 {
					n2 = min(n2, nums[j])
				} else if nums[j] > n2 {
					return true
				}
			}
		}
	}
	return false
}
