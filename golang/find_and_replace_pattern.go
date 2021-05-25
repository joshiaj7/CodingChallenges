package main

// Space : O(len(word))
// Time  : O(n * len(word))

func findAndReplacePattern(words []string, pattern string) []string {
	var ans []string
	pn := len(pattern)

	for _, word := range words {
		if len(word) != pn {
			continue
		}

		mem1, mem2 := make(map[byte]byte), make(map[byte]byte)
		defect := false

		for i := 0; i < pn; i++ {
			if _, ok := mem1[word[i]]; !ok {
				mem1[word[i]] = pattern[i]
			} else if mem1[word[i]] != pattern[i] {
				defect = true
				break
			}

			if _, ok := mem2[pattern[i]]; !ok {
				mem2[pattern[i]] = word[i]
			} else if mem2[pattern[i]] != word[i] {
				defect = true
				break
			}
		}

		if defect == true {
			continue
		}

		if len(mem1) == len(mem2) {
			ans = append(ans, word)
		}

	}

	return ans
}
