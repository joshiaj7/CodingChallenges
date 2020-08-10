package golang

// leetcode
// import "fmt"

func checkValidString(s string) bool {
    firstCheck := 0
    for _, val := range s {
        // fmt.Println(string(val))
        if string(val) == "(" || string(val) == "*"{
            firstCheck++
        } else {
            firstCheck--
        }
        if firstCheck < 0 {
            return false
        }
    }
    
    secondCheck := 0
    for idx := len(s)-1; idx >= 0; idx-- {
        // fmt.Println(string(s[idx]))
        if string(s[idx]) == ")" || string(s[idx]) == "*"{
            secondCheck++
        } else {
            secondCheck--
        }
        if secondCheck < 0 {
            return false
        }
    }
    
    return true
}