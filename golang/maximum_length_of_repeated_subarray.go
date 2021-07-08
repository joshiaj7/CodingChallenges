package main

// Space : O(nm)
// Time  : O(nm)

func findLength(nums1 []int, nums2 []int) int {
    n, m := len(nums1), len(nums2)
	ans := 0
    var dp [][]int
    
    for i := 0; i <= n; i++ {
        var temp []int
        for j := 0; j <= m; j++ {
            temp = append(temp, 0)
        }
        dp = append(dp, temp)
    }
    
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if nums1[i] == nums2[j] {
                dp[i+1][j+1] = dp[i][j] + 1
            }
        }
    }
    
    for i := 0; i <= n; i++ {
        for j := 0; j <= m; j++ {
            ans = Max(ans, dp[i][j])
        }
    }
    
    return ans
}