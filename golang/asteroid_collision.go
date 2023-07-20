package main

/*
Space	: O(n)
Time	: O(n)
*/

func asteroidCollision(asteroids []int) []int {
	stack := []int{}

	for _, ast := range asteroids {
		if len(stack) == 0 {
			stack = append(stack, ast)
			continue
		}

		push := true
		for len(stack) > 0 && stack[len(stack)-1] > 0 && ast < 0 {
			if stack[len(stack)-1] > -ast {
				push = false
				break
			} else if stack[len(stack)-1] < -ast {
				stack = stack[:len(stack)-1]
			} else {
				stack = stack[:len(stack)-1]
				push = false
				break
			}
		}

		if push {
			stack = append(stack, ast)
		}
	}

	return stack
}
