package golang

// Space   : O(1)
// Time    : O(n)

func constructArray(n int, k int) []int {
	s, e := 2, n
	ans := []int{1}

	for s <= e {
		if k > 1 {
			if ans[len(ans)-1] == s-1 {
				ans = append(ans, e)
				e--
			} else {
				ans = append(ans, s)
				s++
			}
			k--
		} else {
			if ans[len(ans)-1] == s-1 {
				ans = append(ans, s)
				s++
			} else {
				ans = append(ans, e)
				e--
			}
		}
	}

	return ans
}
