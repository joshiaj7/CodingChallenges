package main

// Space : O(1)
// Time  : O(1)

func findLUSlength(a string, b string) int {
    if a == b {
        return -1
    }
    
    if len(a) > len(b) {
        return len(a)
    }
    return len(b)
}