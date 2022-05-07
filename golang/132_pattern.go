package main

/*
Space   : O(n)
Time    : O(n)

Method:
Stack

32 is already ordered, only reversed
only need to find the 1
*/

func find132pattern(nums []int) bool {
    n := len(nums)
    n2 := -int(^uint(0) >> 1) - 1
    stack := []int{}
    
    for i := n-1; i >= 0; i-- {
        if nums[i] < n2 {
            return true
        } else {
            for len(stack) > 0 && nums[i] > stack[len(stack)-1] {
                n2 = stack[len(stack)-1]
                stack = stack[:len(stack)-1]
            }
        }
        stack = append(stack, nums[i])
    }
    
    return false
}
