package main

/*
space : O(n)
time  : O(n)

Method:
Sliding window
*/

import (
	"math"
)

func hasAllCodes(s string, k int) bool {
	hashmap := make(map[string]int)
	n := len(s)

	for i := 0; i < (n - k + 1); i++ {
		hashmap[s[i:i+k]] = 1
	}

	return len(hashmap) == int(math.Pow(2, float64(k)))
}
