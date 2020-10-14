package golang

// Space   : O(1)
// Time    : O(n)

func titleToNumber(s string) int {
    res := 0
    leng := len(s)
    
    multiplier := 1
    for i := leng-1; i >= 0; i-- {
        res += multiplier * (int(s[i])-64)
        multiplier *= 26
    }
    
    return res
}