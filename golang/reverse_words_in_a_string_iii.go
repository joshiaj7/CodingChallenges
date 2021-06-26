package main

import "strings"

// Space : O(n)
// Time  : O(n)

func reverseWords(s string) string {
    l := strings.Split(s, " ")
    var ans string
    
    for i := 0; i < len(l); i++ {
        for j := len(l[i])-1; j >= 0; j-- {
            ans += string(l[i][j])
        }
        if i != len(l)-1 {
            ans += " "
        }
    }
    
    return ans
}