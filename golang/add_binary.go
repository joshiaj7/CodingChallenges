package main

import (
	"fmt"
	"strconv"
)

func addBinary(a string, b string) string {
	la, lb := len(a), len(b)
	ll := Max(la, lb)

	if la < ll {
		for i := 0; i < ll-la; i++ {
			a = "0" + a
		}
	}

	if lb < ll {
		for i := 0; i < ll-lb; i++ {
			b = "0" + b
		}
	}

	ans := ""
	rem := 0
	for i := ll - 1; i >= 0; i-- {
		ia, _ := strconv.Atoi(string(a[i]))
		ib, _ := strconv.Atoi(string(b[i]))
		count := ia + ib + rem

		if count == 3 {
			ans = "1" + ans
		} else if count == 2 {
			ans = "0" + ans
			rem = 1
		} else {
			ans = fmt.Sprint(count) + ans
			rem = 0
		}
	}

	if rem == 1 {
		ans = "1" + ans
	}

	return ans
}
