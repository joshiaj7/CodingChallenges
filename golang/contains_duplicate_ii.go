package main

// Space : O(n)
// Time  : O(n)

func containsNearbyDuplicate(nums []int, k int) bool {
    n := len(nums)
    d := make(map[int]int)
    
    for i := 0; i < n; i++ {
        if _, ok := d[nums[i]]; !ok {
            d[nums[i]] = i
        } else {
            if i - d[nums[i]] <= k {
                return true
            }
            d[nums[i]] = i
        }
    } 
    
    return false
}