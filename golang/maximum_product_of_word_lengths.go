package main

// Space : O(n)
// Time  : O(n**2)

func checkContainedKey(a map[byte]int, b map[byte]int) bool {
	for k, _ := range a {
		if _, ok := b[k]; ok {
			return true
		}
	}
	return false
}

func maxProduct(words []string) int {
	word_maps := make([]map[byte]int, 0)
	ans, n := 0, len(words)

	for i := 0; i < n; i++ {
		d := make(map[byte]int, 0)
		m := len(words[i])
		for j := 0; j < m; j++ {
			d[words[i][j]] = 1
		}
		word_maps = append(word_maps, d)
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if !checkContainedKey(word_maps[i], word_maps[j]) {
				ans = Max(ans, len(words[i])*len(words[j]))
			}
		}
	}

	return ans
}
