package main

// Space   : O(n)
// Time    : O(n)

func longestPalindrome(s string) int {
	ans := 0
	hashmap := make(map[string]int)
	hasOdd := false

	for _, val := range s {
		if _, ok := hashmap[string(val)]; ok {
			hashmap[string(val)]++
		} else {
			hashmap[string(val)] = 1
		}
	}

	for _, v := range hashmap {
		if v%2 == 0 {
			ans += v
		} else {
			hasOdd = true
			ans += v - 1
		}
	}

	if hasOdd {
		return ans + 1
	}

	return ans
}
