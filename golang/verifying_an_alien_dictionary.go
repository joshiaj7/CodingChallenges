package main

/**
Space	: O(order)
Time	: O(len(words) * len(words[i]))
**/

func isAlienSorted(words []string, order string) bool {
	d := map[byte]int{}

	for i, c := range order {
		d[byte(c)] = i
	}

	for i := 0; i < len(words)-1; i++ {
		w1, w2 := words[i], words[i+1]

		for j := 0; j < len(w1); j++ {
			if j == len(w2) {
				return false
			}

			if w1[j] != w2[j] {
				if d[w1[j]] > d[w2[j]] {
					return false
				}
				break
			}
		}
	}

	return true
}
