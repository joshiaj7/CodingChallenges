package main

// Space	: O(1)
// Time		: O(n)

import (
	"math"
)

func scoreOfParentheses(S string) int {
	ans, pwr := 0, -1
	isAdded := false

	for _, letter := range S {
		if string(letter) == "(" {
			isAdded = false
			pwr++
		} else {
			if !isAdded {
				ans += int(math.Pow(2.0, float64(pwr)))
				isAdded = true
			}
			pwr--
		}
	}

	return ans
}
