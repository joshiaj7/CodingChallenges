package main

func candy(ratings []int) int {
	n := len(ratings)
	if n == 1 {
		return 1
	}

	var c []int

	// fill c
	for i := 0; i < n; i++ {
		c = append(c, 1)
	}

	// forward
	for i := 1; i < n; i++ {
		if ratings[i] > ratings[i-1] {
			c[i] = Max(c[i], c[i-1]+1)
		}
	}

	// backward
	for i := n - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] {
			c[i] = Max(c[i], c[i+1]+1)
		}
	}

	ans := 0
	for i := 0; i < n; i++ {
		ans += c[i]
	}

	return ans
}
