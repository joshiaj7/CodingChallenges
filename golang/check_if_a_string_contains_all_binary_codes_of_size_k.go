package golang

// space : O(1)
// time  : O(n)

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
