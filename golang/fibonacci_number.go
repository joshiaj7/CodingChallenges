package golang

// Space   : O(n)
// Time    : O(n)

func fib(n int) int {
    mem := []int{0, 1}
    
    if n <= 1 {
        return mem[n]
    }
    
    for i := 2; i <= n; i++ {
        mem = append(mem, mem[i-1] + mem[i-2])
    }
    
    return mem[n]
}