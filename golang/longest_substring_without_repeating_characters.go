package main

// Space	: O(n)
// Time		: O(n)

func lengthOfLongestSubstring(s string) int {
	start, ans := 0, 0
	d := map[byte]int{}

	for i := 0; i < len(s); i++ {
		if _, ok := d[s[i]]; ok && start <= d[s[i]] {
			start = d[s[i]] + 1
		} else {
			ans = Max(ans, i-start+1)
		}
		d[s[i]] = i
	}

	return ans
}
