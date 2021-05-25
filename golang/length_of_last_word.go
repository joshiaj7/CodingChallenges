package main

// Space   : O(1)
// Time    : O(1)

import (
	"strings"
)

func lengthOfLastWord(s string) int {
	ans := 0
	s = strings.TrimSpace(s)

	if len(s) == 0 {
		return ans
	}

	arr := strings.Split(s, " ")

	ans = len(arr[len(arr)-1])

	return ans
}
