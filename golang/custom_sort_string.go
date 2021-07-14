package main

import (
	"sort"
	"strings"
)

// Space	: O(n)
// Time		: O(n log n)

func customSortString(order string, str string) string {
    d := make(map[string]int)

    for i := 0; i < len(order); i++ {
        d[string(order[i])] = i
    }
    
    idx := len(order)
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    for j := 0; j < 26; j++ {
        if _, ok := d[string(alphabet[j])]; !ok {
            d[string(alphabet[j])] = idx
            idx++
        } 
    } 
    
    s := strings.Split(str, "")
    sort.Slice(s, func(i, j int) bool { 
        return d[s[i]] < d[s[j]]
    })
    
    return strings.Join(s, "")
}