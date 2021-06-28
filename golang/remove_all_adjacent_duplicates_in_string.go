package main

// Space : O(n)
// Time  : O(n)

func removeDuplicates(s string) string {
    var stack []byte
    n := len(s)
    
    for i := 0; i < n; i++ {
        if len(stack) > 0 && stack[len(stack)-1] == s[i] {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, s[i])
        }
    }
    
    return string(stack)
}