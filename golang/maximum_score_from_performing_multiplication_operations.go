package main

/*
Space	: O(m^2)
Time	: O(m^2)

DP approach
*/

func maximumScore(nums []int, multipliers []int) int {
    n, m := len(nums), len(multipliers)
    var dp [][]int
    
    for i := 0; i < m+1; i++ {
        var temp []int
        for j := 0; j < m+1; j++ {
            temp = append(temp, 0)
        }
        dp = append(dp, temp)
    }
    
    for i := m-1; i >= 0; i-- {
        for j := i; j >= 0; j-- {
            mul := multipliers[i]
            left := j
            right := n - 1 - (i - j)
            dp[i][j] = Max((mul * nums[left]) + dp[i+1][j+1], (mul * nums[right]) + dp[i+1][j])            
        }
    }
    
    return dp[0][0]
}
