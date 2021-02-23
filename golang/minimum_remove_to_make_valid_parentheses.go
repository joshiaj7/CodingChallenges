package golang

// Space 	: O(n)
// Time		: O(n)

func minRemoveToMakeValid(s string) string {
	ans := []byte(s)
	var indices []int

	for i := 0; i < len(ans); i++ {
		if string(s[i]) == "(" {
			indices = append(indices, i)
		} else if string(s[i]) == ")" {
			if len(indices) > 0 {
				indices = indices[:len(indices)-1]
			} else {
				ans[i] = 0
			}
		}
	}

	for j := 0; j < len(indices); j++ {
		ans[indices[j]] = 0
	}

	newStr := ""
	for k := 0; k < len(ans); k++ {
		if ans[k] > 0 {
			newStr += string(ans[k])
		}
	}

	return newStr
}
