package main

// Space	: O(2n)
// Time		: O(2n)

func generate(numRows int) [][]int {
    var ans [][]int
    
    for i := 1; i <= numRows; i++ {
        var row []int
        for j := 1; j <= i; j++ {
            if j == 1 || j == i {
                row = append(row, 1)
            } else {
                row = append(row, ans[i-2][j-2] + ans[i-2][j-1])
            }
        }
        ans = append(ans, row)
    }
    
    return ans
}