package main

// Space : O(1)
// Time  : O(n)

func numSubarrayBoundedMax(nums []int, left int, right int) int {
    ans, bucket1, bucket2 := 0, 0, 0
    
    for _, x := range nums {
        if x < left {
            bucket1++
        } else {
            bucket1 = 0
        }
        if x <= right {
            bucket2++
        } else {
            bucket2 = 0
        }
        ans += bucket2 - bucket1
    
    }
    
    return ans
}