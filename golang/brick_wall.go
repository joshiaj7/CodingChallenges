package main

func leastBricks(wall [][]int) int {
	if len(wall) == 0 {
		return 0
	}
	if len(wall[0]) == 0 {
		return 0
	}

	d := map[int]int{}

	for _, row := range wall {
		width := 0
		for i := 0; i < len(row); i++ {
			width += row[i]
			if i < len(row)-1 {
				if _, ok := d[width]; ok {
					d[width] += 1
				} else {
					d[width] = 1
				}
			}
		}
	}

	ans := len(wall)
	for _, val := range d {
		ans = Min(len(wall)-val, ans)
	}

	return ans
}
