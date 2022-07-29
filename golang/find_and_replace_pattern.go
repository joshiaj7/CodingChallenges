package main

/*
Space : O(len(word))
Time  : O(n * len(word))
*/

func findAndReplacePattern(words []string, pattern string) []string {
	var ans []string
	n := len(words)

	for i := 0; i < n; i++ {
		word := words[i]
		mem_w := make(map[byte]byte)
		mem_p := make(map[byte]byte)
		safe := true

		for j := 0; j < len(word); j++ {
			w := word[j]
			p := pattern[j]

			_, okw := mem_w[w]
			_, okp := mem_p[p]

			if !okw && !okp {
				mem_w[w] = p
				mem_p[p] = w
			} else if okw && okp && mem_w[w] == p && mem_p[p] == w {
				continue
			} else {
				safe = false
				break
			}
		}

		if !safe {
			continue
		}
		ans = append(ans, word)

	}

	return ans
}
