import (
    "fmt"
    "strings"
)

func lengthOfLastWord(s string) int {
    ans := 0
    s = strings.TrimSpace(s)
    
    if len(s) == 0 {
        return ans
    }
    
    arr := strings.Split(s, " ")
    
    ans = len(arr[len(arr)-1])
    
    return ans
}