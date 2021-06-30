package main

// Space : O(1)
// Time  : O(n)

func minMoves(nums []int) int {
    ans, min_num := 0, nums[0]
    
    for _, x := range nums {
        min_num = Min(min_num, x)
    }
    
    for _, x := range nums {
        ans += x - min_num
    }
    
    return ans
}