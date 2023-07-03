package main

/*
Space	: O(n)
Time	: O(n)
*/

func buddyStrings(s string, goal string) bool {
	n := len(s)

	if n != len(goal) {
		return false
	}

	h1, h2 := map[string]int{}, map[string]int{}
	dif := 0
	for i := 0; i < n; i++ {
		if s[i] != goal[i] {
			dif += 1
		}

		if _, ok := h1[string(s[i])]; ok {
			h1[string(s[i])]++
		} else {
			h1[string(s[i])] = 1
		}

		if _, ok := h2[string(goal[i])]; ok {
			h2[string(goal[i])]++
		} else {
			h2[string(goal[i])] = 1
		}
	}

	multi := false
	for k, v := range h1 {
		if _, ok := h2[k]; ok {
			if h2[k] != v {
				return false
			}
		} else {
			return false
		}

		if v > 1 {
			multi = true
		}
	}

	if multi && dif <= 2 {
		return true
	}

	if dif == 2 {
		return true
	}

	return false
}
