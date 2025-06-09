package main

func getLongestSubsequence(words []string, groups []int) []string {
	ans := []string{}
	n := len(words)

	currGroup := 0
	for i := range n {
		if i == 0 || currGroup != groups[i] {
			ans = append(ans, words[i])
			currGroup = groups[i]
		}
	}

	return ans
}
