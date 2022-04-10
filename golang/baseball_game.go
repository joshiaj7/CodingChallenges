package main

// Space: O(n)
// Time	: O(n)

import "strconv"

func calPoints(ops []string) int {
    var stack []int
    ans := 0
    
    for _, x := range ops {
        if x == "C" {
            stack = stack[:len(stack)-1]
        } else if x == "D" {
            stack = append(stack, stack[len(stack)-1] * 2)
        } else if x == "+" {
            stack = append(stack, stack[len(stack)-1] + stack[len(stack)-2])
        } else {
            num, _ := strconv.Atoi(x)
            stack = append(stack, num)
        }
    }    
    
    for _, r := range stack {
        ans += r
    }
    
    return ans
}
