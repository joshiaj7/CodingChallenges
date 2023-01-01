package main

import "strings"

/*
Space	: O(n)
Time	: O(n)
*/

func wordPattern(pattern string, s string) bool {
	d1 := map[byte]string{}
	d2 := map[string]byte{}
	n := len(pattern)
	strs := strings.Split(s, " ")

	if len(strs) != n {
		return false
	}

	for i := 0; i < n; i++ {
		if _, ok := d1[pattern[i]]; ok {
			if d1[pattern[i]] != strs[i] {
				return false
			}
		}
		if _, ok := d2[strs[i]]; ok {
			if d2[strs[i]] != pattern[i] {
				return false
			}
		}
		d1[pattern[i]] = strs[i]
		d2[strs[i]] = pattern[i]
	}

	return true
}
