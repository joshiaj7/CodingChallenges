package main

func concatenatedBinary(n int) int {
	ans := 0
	mod := 1000000007
	power := 2
	shift := 1

	for i := 1; i <= n; i++ {
		if i == power {
			power *= 2
			shift++
		}
		ans = ((ans << shift) + i) % mod
	}

	return ans
}
