package main

import (
	"fmt"
)

func addDigits(num int) int {
	for true {
		num_str := fmt.Sprint(num)
		num = 0
		for _, c := range num_str {
			num += int(c) - 48
		}

		num_str = fmt.Sprint(num)
		if len(num_str) == 1 {
			return num
		}
	}
	return num
}
