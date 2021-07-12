package main

// Space   : O(n)
// Time    : O(n)

func isIsomorphic(s string, t string) bool {
    s_map, t_map :=  make(map[byte]byte), make(map[byte]byte)
    n := len(s)
    
    for idx := 0; idx < n; idx++ {
        if _, s_ok :=  s_map[s[idx]]; !s_ok {
            s_map[s[idx]] = t[idx]
            if _, t_ok := t_map[t[idx]]; t_ok {
                if t_map[t[idx]] != s[idx] {
                    return false
                }
            } else {
                t_map[t[idx]] = s[idx]
            }
        } else {
            if s_map[s[idx]] != t[idx] {
                return false
            }
        }
    }
    
    return true
}
