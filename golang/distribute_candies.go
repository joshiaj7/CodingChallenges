package main

// Space   : O(n)
// Time    : O(n)

func distributeCandies(candyType []int) int {
	typesD := make(map[int]int)

	for _, ctype := range candyType {
		if _, ok := typesD[ctype]; ok {
			typesD[ctype]++
		} else {
			typesD[ctype] = 1
		}
	}

	return Min(len(candyType)/2, len(typesD))
}
