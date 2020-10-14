package golang

// Space   : O(1)
// Time    : O(n)

import (
    "strings"
)

func isPalindrome(s string) bool {
    clean := ""
    palin := true
    
    for _, l := range strings.ToLower(s) {
        if (l >= 97 && l <= 122) || (l >= 48 && l <= 57) {
            clean += string(l)
        }
    }
    
    leng := len(clean)

    for i := 0; i < leng; i++ {
        if clean[i] != clean[leng-1-i] {
            palin = false
            break
        }
    }
    
    return palin
}