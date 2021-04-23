package golang

// Space : O(1)
// Time : O(n)

func countBinarySubstrings(s string) int {
	ans := 0
	zero, one := 0, 0
	n := len(s)

	last := string(s[0])
	if last == "0" {
		zero++
	} else {
		one++
	}

	for i := 1; i < n; i++ {
		if string(s[i]) != last {
			ans += Min(one, zero)
			if string(s[i]) == "0" {
				zero = 1
			} else {
				one = 1
			}
		} else {
			if string(s[i]) == "0" {
				zero++
			} else {
				one++
			}
		}
		last = string(s[i])
	}

	ans += Min(one, zero)
	return ans
}
