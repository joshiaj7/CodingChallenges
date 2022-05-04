package main

// Space	: O(n)
// Time		: O(n)

func maxOperations(nums []int, k int) int {
	d := make(map[int]int)
	ans := 0

	for _, x := range nums {
		if _, ok := d[x]; ok {
			d[x]++
		} else {
			d[x] = 1
		}
	}

	for key, val := range d {
		if _, ok := d[k-key]; ok {
			count := 0
			if key*2 == k {
				count = val / 2
				d[key] %= 2
			} else {
				count = Min(val, d[k-key])
				d[key] -= count
				d[k-key] -= count
			}
			ans += count
		}
	}

	return ans
}
