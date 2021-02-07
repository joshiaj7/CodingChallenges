package golang

func shortestToChar(s string, c byte) []int {
	var ans, indices []int
	n := len(s)

	for i := 0; i < n; i++ {
		if s[i] == c {
			indices = append(indices, i)
		}
	}

	start, end := -1, indices[0]
	indices = indices[1:]

	for i := 0; i < n; i++ {
		if start >= 0 && end >= 0 {
			ans = append(ans, Min(i-start, end-i))
		} else if start == -1 {
			ans = append(ans, end-i)
		} else {
			ans = append(ans, i-start)
		}

		if i == end {
			start = end
			if len(indices) == 0 {
				end = -1
			} else {
				end = indices[0]
				indices = indices[1:]
			}

		}
	}

	return ans
}