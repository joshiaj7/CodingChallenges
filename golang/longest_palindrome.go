package golang

// leetcode

import (
    "fmt"
)

func longestPalindrome(s string) int {
    ans := 0
    hashmap := make(map[string]int)
    hasOdd := false
    
    for _, val := range s {
        if _, ok := hashmap[string(val)]; ok {
            hashmap[string(val)]++
        } else {
            hashmap[string(val)] = 1
        }
    }
    
    fmt.Printf("hashmap : %v\n", hashmap)
    
    for _, v := range hashmap {
        if v % 2 == 0 {
            ans += v
        } else {
            hasOdd = true
            ans += v-1
        } 
    }
    fmt.Println(ans)
    fmt.Println(hasOdd)
    
    if hasOdd {
        return ans + 1
    } else {
        return ans
    }
}