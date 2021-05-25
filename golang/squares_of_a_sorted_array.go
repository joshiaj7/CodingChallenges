package main

// Space	: O(n)
// Time		: O(n)

func sortedSquares(nums []int) []int {
	var temp1, temp2, ans []int
	n := len(nums)

	i := 0
	for i < n {
		if nums[i] < 0 {
			temp1 = append([]int{nums[i] * nums[i]}, temp1...)
		} else {
			temp2 = append(temp2, nums[i]*nums[i])
		}
		i++
	}

	if len(temp1) == 0 {
		return temp2
	} else if len(temp2) == 0 {
		return temp1
	}

	x, y := 0, 0
	for x < len(temp1) && y < len(temp2) {
		if temp1[x] < temp2[y] {
			ans = append(ans, temp1[x])
			x++
		} else {
			ans = append(ans, temp2[y])
			y++
		}
	}

	if x == len(temp1) {
		ans = append(ans, temp2[y:]...)
	}
	if y == len(temp2) {
		ans = append(ans, temp1[x:]...)
	}

	return ans
}
