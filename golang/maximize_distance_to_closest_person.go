package main

// Space : O(1)
// Time	: O(n)

func maxDistToClosest(seats []int) int {
	var forward, backward, dist, mid, ans int

	n := len(seats)

	for k, v := range seats {
		// forward
		if v == 0 {
			forward++
			dist = Max(dist, forward)
		} else {
			forward = 0
		}

		// backward
		if seats[n-1-k] == 0 {
			backward++
		} else {
			backward = 0
		}

	}

	if dist%2 == 0 {
		mid = dist / 2
	} else {
		mid = (dist + 1) / 2
	}

	ans = Max(ans, mid)
	ans = Max(ans, forward)
	ans = Max(ans, backward)
	return ans
}
