package main

// Space : O(1)
// Time  : O(2^x + 3^y + 5^z)

func isUgly(n int) bool {
    if n == 0 {
        return false
    }
    
    for n % 2 == 0 {
        n /= 2
    }
    
    for n % 3 == 0 {
        n /= 3
    }
    
    for n % 5 == 0 {
        n /= 5
    }
    
    if n == 1 {
        return true
    }
    
    return false
}