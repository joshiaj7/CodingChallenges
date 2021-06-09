package main

import "fmt"

// Space : O(1)
// Time  : O(bin len)

func binaryGap(n int) int {
    b := fmt.Sprintf("%b", n)
    b_len := len(b)
    s, ans := 0, 0
    
    for i := 1; i<b_len; i++ {
        if string(b[i]) == "1" {
            ans = Max(ans, i-s)
            s = i
        }
    }
    
    return ans
}