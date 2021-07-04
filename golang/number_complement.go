package main

import (
	"math"
	"strconv"
)

// Space : O(1)
// Time  : O(1)

func findComplement(num int) int {
    bits := len(strconv.FormatInt(int64(num), 2))
    n := int(math.Pow(2, float64(bits)))-1
    return num ^ n
}