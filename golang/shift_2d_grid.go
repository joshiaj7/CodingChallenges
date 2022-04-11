package main

// Space   : O(m*n)
// Time    : O(m*n)

func shiftGrid(grid [][]int, k int) [][]int {
    row := len(grid)
    col := len(grid[0])
    nm := row * col
    k %= nm
    var temp []int
    
    for _, x := range grid {
        temp = append(temp, x...)
    }
    temp = append(temp[nm-k:], temp[:nm-k]...)

    
    p := 0
    for y := 0; y < row; y++ {
        for x := 0; x < col; x++ {
            grid[y][x] = temp[p]
            p++
        }
    }
    
    return grid
}
