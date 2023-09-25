package main

// Space	: O(n)
// Time		: O(n)

func findTheDifference(s string, t string) byte {
	if len(t) > len(s) {
		s, t = t, s
	}

	var def byte
	_, n := len(s), len(t)
	smap := map[byte]int{}
	tmap := map[byte]int{}

	i := 0
	for i < n {
		smap[s[i]]++
		tmap[t[i]]++
		i++
	}

	smap[s[i]]++

	for k, v := range smap {
		if _, ok := tmap[k]; !ok {
			return k
		}
		if v != tmap[k] {
			return k
		}
	}

	return def
}
