package main

import (
	"fmt"
	"strconv"
)

/*
Space	: O(1)
Time	: O(n)
*/

func decodeAtIndex(s string, k int) string {
	size := 0
	n := len(s)

	for i := 0; i < n; i++ {
		if dig, err := strconv.Atoi(string(s[i])); err == nil {
			size *= dig
		} else {
			size++
		}
	}

	fmt.Println(size)
	for j := n - 1; j >= 0; j-- {
		k %= size

		dig, err := strconv.Atoi(string(s[j]))

		if err != nil {
			if k == 0 {
				return string(s[j])
			}
			size--
		} else {
			size /= dig
		}
	}

	return string(s[k])
}
