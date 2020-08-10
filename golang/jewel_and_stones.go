package golang

// leetcode
// import "fmt"

func numJewelsInStones(J string, S string) int {
    res := 0
    hashmap := make(map[string]int)
    
    for _, item := range S {
        // fmt.Println(string(item))
        if _, ok := hashmap[string(item)]; ok {
            hashmap[string(item)]++
        } else {
            hashmap[string(item)] = 1
        }
    }
    
    for _, item := range J {
        if val, ok := hashmap[string(item)]; ok {
            res += val
        } 
    }
    
    return res
}