package main

// Space :	O(n)
// Time	 :	O(n)

func isValid(s string) bool {
	stack := []string{}

	for _, c := range s {
		chr := string(c)

		if len(stack) == 0 {
			stack = append(stack, chr)
			continue
		}

		if chr == "(" || chr == "{" || chr == "[" {
			stack = append(stack, chr)
		} else {
			if stack[len(stack)-1] == "(" && chr == ")" {
				stack = stack[:len(stack)-1]
			} else if stack[len(stack)-1] == "{" && chr == "}" {
				stack = stack[:len(stack)-1]
			} else if stack[len(stack)-1] == "[" && chr == "]" {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		}
	}

	if len(stack) > 0 {
		return false
	}

	return true
}
