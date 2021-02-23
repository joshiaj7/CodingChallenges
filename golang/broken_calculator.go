package golang

func brokenCalc(X int, Y int) int {
	ans := 0
	for Y > X {
		if Y%2 == 1 {
			Y++
			ans++
		}
		Y /= 2
		ans++
	}

	return ans + (X - Y)
}
