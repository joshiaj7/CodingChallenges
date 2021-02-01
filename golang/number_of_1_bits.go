package golang

func hammingWeight(num uint32) int {
	ans := 0

	for num > 0 {
		if num%2 == 1 {
			ans++
		}
		num /= 2
	}

	return ans
}