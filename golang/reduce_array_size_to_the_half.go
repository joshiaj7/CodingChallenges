package main

import "sort"

/*
Space : O(n)
Time  : O(n log n)
*/

func minSetSize(arr []int) int {
	n, target := len(arr), len(arr)/2
	d := make(map[int]int)

	for _, x := range arr {
		if _, ok := d[x]; ok {
			d[x]++
		} else {
			d[x] = 1
		}
	}

	var temp []int
	for _, v := range d {
		temp = append(temp, v)
	}

	i, count := 0, 0
	sort.Sort(sort.Reverse(sort.IntSlice(temp)))

	for i < n && count < target {
		count += temp[i]
		i++
	}

	return i
}
