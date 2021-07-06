package main

import "sort"

// Space : O(n)
// Time  : O(n log n)

func minSetSize(arr []int) int {
	n, ans := len(arr), 0
	h := n / 2
	d := make(map[int]int)

	for _, x := range arr {
		if _, ok := d[x]; ok {
			d[x]++
		} else {
			d[x] = 1
		}
	}

	freq := []int{}
	for _, val := range d {
		freq = append(freq, val)
	}

	sort.Slice(freq, func(i, j int) bool {
		return freq[i] > freq[j]
	})

	for _, f := range freq {
		if n > h {
			n -= f
			ans++
		} else {
			break
		}
	}

	return ans
}