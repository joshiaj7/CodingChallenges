package golang

// Space	: O(k)
// Time	: O(n)

func rotate(nums []int, k int) {
	n := len(nums)
	k %= n
	var temp []int

	for i := 0; i < k; i++ {
		temp = append(temp, nums[n-k+i])
	}

	for j := n - 1; j >= 0; j-- {
		if j >= k {
			nums[j] = nums[j-k]
		} else {
			nums[j] = temp[j]
		}

	}
}
