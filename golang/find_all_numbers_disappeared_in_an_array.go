package main

// Space : O(n)
// Time  : O(n)

func findDisappearedNumbers(nums []int) []int {
    ans := []int{}
    n := len(nums)
    d := make(map[int]int)
    
    for _, v := range nums {
        d[v] = 1
    }
    
    for i := 1; i <= n; i++ {
        if _, ok := d[i]; !ok {
            ans = append(ans, i)
        }
    } 
    
    return ans
}