package main

import (
	"fmt"
	"math"
	"strconv"
)

func intToRoman(num int) string {
	ans := ""
	truth := map[int]string{
		1:    "I",
		4:    "IV",
		5:    "V",
		9:    "IX",
		10:   "X",
		40:   "XL",
		50:   "L",
		90:   "XC",
		100:  "C",
		400:  "CD",
		500:  "D",
		900:  "CM",
		1000: "M",
	}

	n := len(strconv.Itoa(num))
	multi := int(math.Pow(10, float64(n-1)))

	for i := 0; i < n; i++ {
		temp, _ := strconv.Atoi(string(strconv.Itoa(num)[i]))
		fmt.Println(temp)

		for temp > 0 {
			if temp == 9 {
				ans += truth[9*multi]
				temp -= 9
			} else if temp >= 5 {
				ans += truth[5*multi]
				temp -= 5
			} else if temp >= 4 {
				ans += truth[4*multi]
				temp -= 4
			} else if temp >= 1 {
				ans += truth[1*multi]
				temp -= 1
			}
		}
		multi /= 10
	}

	return ans
}
