package golang

// Space   : O(n)
// Time    : O(n)

import (
    "fmt"
    "strings"
)

func toGoatLatin(S string) string {
    var ans, first, ma string
    words := strings.Split(S, " ")
    
    for idx, val := range words {
        ma = "ma"
        first = strings.ToLower(string(val[0]))
        
        // build ma
        ma = ma + strings.Repeat("a", idx + 1)
        
        // flip string
        if (first != "a") && (first != "e") && (first != "i") && (first != "o") && (first != "u") {
            if len(val) > 1 {
                val = val[1:] + string(val[0])
            }
        }
        
        // add everything up
        ans += val + ma
        if idx != len(words) - 1 {
            ans += " "            
        } 
        fmt.Println(ans)
    }
    
    return ans
}