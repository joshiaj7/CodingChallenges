package main

// Space : O(c)
// Time  : O(r*c)

func matrixReshape(mat [][]int, r int, c int) [][]int {
    row := len(mat)
    col := len(mat[0])
    
    if row*col != r*c {
        return mat
    }
    
    ans, temp := [][]int{}, []int{}
    for y := 0; y < row; y++ {
        for x := 0; x < col; x++ {
            temp = append(temp, mat[y][x])
            if len(temp) == c {
                ans = append(ans, temp)
                temp = []int{}
            }
        }
    }
    
    return ans
}