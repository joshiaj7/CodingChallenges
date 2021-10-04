package main

import "fmt"

// Space	: O(1)
// Time		: O(n)

func isPowerOfTwo(n int) bool {
	if n < 0 {
		return false
	}

	b := fmt.Sprintf("%b", n)
	ones := 0

	for i := 0; i < len(b); i++ {
		if b[i] == 49 {
			ones++
		}
	}

	return ones == 1
}
