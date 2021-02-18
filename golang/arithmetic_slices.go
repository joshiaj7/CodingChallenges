package golang

func numberOfArithmeticSlices(A []int) int {
	ans := 0
	var temp []int
	n := len(A)

	if n < 3 {
		return 0
	}

	for i := 1; i < n; i++ {
		temp = append(temp, A[i]-A[i-1])
	}

	count := 0
	for j := 1; j < len(temp); j++ {
		if temp[j] == temp[j-1] {
			count++
		} else {
			count = 0
		}
		ans += count
	}

	return ans
}