package main

import "strings"

func makeFancyString(s string) string {
	stack := []string{}

	for _, l := range s {
		let := string(l)

		if len(stack) >= 2 {
			n := len(stack)
			if stack[n-1] == stack[n-2] && stack[n-1] == let {
				continue
			} else {
				stack = append(stack, let)
			}
		} else {
			stack = append(stack, let)
		}
	}

	return strings.Join(stack, "")
}
