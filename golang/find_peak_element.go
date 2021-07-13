package main

// Space	: O(1)
// Time		: O(log n)

func findPeakElement(nums []int) int {
    n := len(nums)
    
    if n == 1 {
        return 0
    }
    
    start, end := 0, n-1
    
    for start < end {
        mid1 := (start + end) / 2
        mid2 := mid1 + 1
        
        if nums[mid1] < nums[mid2] {
            start = mid2
        } else {
            end = mid1
        }
    }
    
    return start
}