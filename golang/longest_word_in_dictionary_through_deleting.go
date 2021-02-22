package golang

// Space	: O(1)
// Time		: O(n^2)

func findLongestWord(s string, d []string) string {
    ans := ""
    
    for _, word := range d {
        a, b := len(word), len(ans)
        if a < b || (a == b && word > ans) { 
            continue
        }
        
        i := 0
        for _, c := range s {
            if byte(c) == word[i] {
                i++
            }
            
            if i == a {
                ans = word
                break
            }   
        }
    }
    
    
    return ans
}