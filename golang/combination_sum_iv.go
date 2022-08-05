package main

import "sort"

/*
Space	: O(n)
Time	: O(t * n)
*/

func combinationSum4(nums []int, target int) int {
    sort.Ints(nums)
    var dp []int
    
    for i := 0; i <= target; i++ {
        if i == 0 {
            dp = append(dp, 1)
        } else {
            dp = append(dp, 0)
        }
    } 
    
    for i := 0; i <= target; i++ {
        for _, n := range nums {
            if n > i {
                break
            }
            if n == i {
                dp[i]++
            } 
            if n < i {
                dp[i] += dp[i-n]
            }
        }
    }
    
    return dp[len(dp)-1]
}
