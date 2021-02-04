package golang

func findLHS(nums []int) int {
	ans := 0
	d := make(map[int]int)

	for _, v := range nums {
		if _, ok := d[v]; ok {
			d[v]++
		} else {
			d[v] = 1
		}
	}

	for k := range d {
		if _, ok := d[k+1]; ok {
			ans = Max(ans, d[k]+d[k+1])
		}
	}

	return ans
}
