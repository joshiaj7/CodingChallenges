package main

// DP Approach
// Space : O(m*n)
// Time  : O(m*n)

func isInterleave(s1 string, s2 string, s3 string) bool {
    l1, l2, l3 := len(s1), len(s2), len(s3)
    
    if l1 + l2 != l3 {
        return false
    }
    
    var dp [][]bool
    for y := 0; y < l1 + 1; y++ {
        var row []bool
        for x := 0; x < l2 + 1; x++ {
            row = append(row, false)
        }
        dp = append(dp, row)
    }
    
    for y := 0; y < l1 + 1; y++ {
        for x := 0; x < l2 + 1; x++ {
            if y == 0 && x == 0 {
                dp[y][x] = true
            } else if y == 0 {
                dp[y][x] = dp[y][x-1] && s3[y+x-1] == s2[x-1]
            } else if x == 0 {
                dp[y][x] = dp[y-1][x] && s3[y+x-1] == s1[y-1]
            } else {
                dp[y][x] = (dp[y][x-1] && s3[y+x-1] == s2[x-1]) || (dp[y-1][x] && s3[y+x-1] == s1[y-1])
            }
        }
    }
    
    
    return dp[l1][l2]
}