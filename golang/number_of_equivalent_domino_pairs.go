package main

type IntPair struct {
	First  int
	Second int
}

func numEquivDominoPairs(dominoes [][]int) int {
	ans := 0
	d := map[IntPair]int{}

	for _, domino := range dominoes {
		first, second := domino[0], domino[1]

		if v, ok := d[IntPair{First: first, Second: second}]; ok {
			ans += v * 1
			d[IntPair{First: first, Second: second}]++
		} else if v, ok2 := d[IntPair{First: second, Second: first}]; ok2 {
			ans += v * 1
			d[IntPair{First: second, Second: first}]++
		} else {
			d[IntPair{First: first, Second: second}] = 1
		}
	}

	return ans
}
