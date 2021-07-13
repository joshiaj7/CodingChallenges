package main

// Space	: O(1)
// Time		: O(26 log n)

func convertToTitle(c int) string {
    ans := ""
    
    for c > 0 {
        c--
        ans = string(byte(65+(c % 26))) + ans
        c /= 26
    }
    
    return ans
}
