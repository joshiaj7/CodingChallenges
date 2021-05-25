package main

// Space 	: O(1)
// Time	    : O(n)

import (
	"unicode"
)

func halvesAreAlike(s string) bool {
	v1, v2 := 0, 0
	n := len(s)
	vowels := map[rune]int{
		'a': 1,
		'e': 1,
		'i': 1,
		'o': 1,
		'u': 1,
	}

	for i := 0; i < n/2; i++ {
		if _, ok := vowels[unicode.ToLower(rune(s[i]))]; ok {
			v1++
		}
		if _, ok := vowels[unicode.ToLower(rune(s[i+(n/2)]))]; ok {
			v2++
		}

	}

	return v1 == v2
}
