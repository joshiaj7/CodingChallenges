package main

/*
Space	: O(1)
Time	: O(n)
*/

func romanToInt(s string) int {
	rmap := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	ans := 0
	n := len(s)

	for i := 0; i < n-1; i++ {
		if rmap[s[i]] >= rmap[s[i+1]] {
			ans += rmap[s[i]]
		} else {
			ans -= rmap[s[i]]
		}
	}

	ans += rmap[s[n-1]]
	return ans
}
