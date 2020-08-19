import (
    "fmt"
    "strings"
)

// leetcode

func toGoatLatin(S string) string {
    var ans, first_letter, ma string
    words := strings.Split(S, " ")
    
    for idx, val := range words {
        ma = "ma"
        first_letter = strings.ToLower(string(val[0]))
        
        // build ma
        ma = ma + strings.Repeat("a", idx + 1)
        
        // flip string
        if (first_letter != "a") && (first_letter != "e") && (first_letter != "i") && (first_letter != "o") && (first_letter != "u") {
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