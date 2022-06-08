package main

/*
Space	: O(1)
Time	: O(n)
*/

func removePalindromeSub(s string) int {
    start, end :=  0, len(s)-1
    palindrome := true
    for start < end {
        if s[start] != s[end] {
            palindrome = false
            break
        }
        start++
        end--
    }
    
    if !palindrome && len(s) > 0 {
        return 2
    } else if len(s) > 0 || palindrome {
        return 1
    } 
    return 0
}
