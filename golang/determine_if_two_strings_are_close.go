package main

/*
Space	: O(n)
Time	: O(n)
*/

func closeStrings(word1 string, word2 string) bool {
	h1, h2 := map[rune]int{}, map[rune]int{}
	c1, c2 := map[int]int{}, map[int]int{}

	for _, c := range word1 {
		h1[c]++
	}

	for _, c := range word2 {
		h2[c]++
	}

	for k, v := range h1 {
		if _, ok := h2[k]; !ok {
			return false
		}
		c1[v]++
	}

	for k, v := range h2 {
		if _, ok := h1[k]; !ok {
			return false
		}
		c2[v]++
	}

	for k, v := range c1 {
		if _, ok := c2[k]; !ok {
			return false
		}

		if c2[k] != v {
			return false
		}
	}

	return true
}
