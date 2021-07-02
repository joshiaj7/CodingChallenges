package main

// Space : O(2^n)
// Time  : O(2^n)

func grayCode(n int) []int {
    ans := []int{0}
    
    for i := 1; i <= n; i++ {
        prev_len := len(ans)
        mask := 1 << (i-1)
        for j := prev_len; j > 0; j-- {
            ans = append(ans, mask + ans[j-1])
        }
    }
    return ans
}