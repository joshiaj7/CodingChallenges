package golang

// Space   : O(1)
// Time    : O(n**2)

func findMaximumXOR(nums []int) int {
	ans := 0

	for i := 0; i < len(nums); i++ {
		for j := i; j < len(nums); j++ {
			if ans < nums[i]^nums[j] {
				ans = nums[i] ^ nums[j]
			}
		}
	}

	return ans
}
