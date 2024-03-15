package main

/*
Space  : O(n)
Time   : O(n)
*/

func productExceptSelf(nums []int) []int {
    n := len(nums)
    pref := make([]int, n)
    suf := make([]int, n)
    ans := make([]int, n)

    for i := 0; i < n; i++ {
        if i == 0 {
            pref[i] = nums[i]
            suf[n-i-1] = nums[n-i-1]
        } else {
            pref[i] = pref[i-1] * nums[i]
            suf[n-i-1] = suf[n-i] * nums[n-i-1]
        }
    }

    for i := 0; i < n; i++ {
        if i == 0 {
            ans[i] = suf[i+1]
        } else if i == n-1 {
            ans[i] = pref[i-1]
        } else {
            ans[i] = pref[i-1] * suf[i+1]
        }
    }

    return ans
}
