package golang

import (
	"strconv"
	"strings"
)

func getSmallestString(n int, k int) string {
	zs := 0

	for k-26 >= n-1 {
		zs++
		k -= 26
		n--
	}

	var mid string
	if k > n {
		mid = strconv.Itoa(96 + k - n + 1)
		k = k - n + 1
		n--
	}

	return strings.Repeat("a", n) + mid + strings.Repeat("z", zs)

}
