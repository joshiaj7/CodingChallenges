package main

// Space   : O(n)
// Time    : O(n)

import (
	"strconv"
)

func fizzBuzz(n int) []string {
	var ans []string
	var item string

	for i := 0; i < n; i++ {
		item = ""
		if (i+1)%3 == 0 {
			item += "Fizz"
		}
		if (i+1)%5 == 0 {
			item += "Buzz"
		}
		if item == "" {
			item = strconv.Itoa(i + 1)
		}
		ans = append(ans, item)
	}

	return ans
}
