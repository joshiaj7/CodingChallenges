package main

// Space	: O(1)
// Time		: O(log n)

func divide(dividend int, divisor int) int {
	if dividend == 0 {
		return 0
	}

	isNeg1 := dividend < 0
	isNeg2 := divisor < 0
	isNeg := isNeg1 != isNeg2

	if dividend < 0 {
		dividend *= -1
	}
	if divisor < 0 {
		divisor *= -1
	}

	ans, count, temp := 0, 1, divisor
	for (divisor << 1) <= dividend {
		divisor <<= 1
		count <<= 1
	}

	for (dividend >= divisor) && (dividend > 0) {
		dividend -= divisor
		ans += count
		for dividend < divisor {
			divisor >>= 1
			count >>= 1
		}
		if divisor < temp {
			break
		}
	}

	if isNeg {
		return -1 * Min(ans, 2147483648)
	}

	return Min(ans, 2147483647)
}
