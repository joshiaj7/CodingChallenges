package main

// Space : O(1)
// Time  : O(log n)

func isPerfectSquare(n int) bool {
    i := 1
    
    for i*i <= n {
        if i*i == n {
            return true
        }
        i++
    }
    
    return false
}