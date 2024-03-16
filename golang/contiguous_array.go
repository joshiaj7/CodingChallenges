package main

/*
Space  : O(n)
Time   : O(n)
*/

func findMaxLength(nums []int) int {
    ans := 0
    sumMap := map[int]int{}
    n :=  len(nums)
    arr := make([]int, n)

    for idx, val := range nums {
        sub := 0
        if val == 1 {
            sub = 1
        } else {
            sub = -1
        }

        if idx == 0 {
            arr[idx] = sub
        } else {
            arr[idx] = arr[idx-1] + sub
        }

        if _, ok := sumMap[arr[idx]]; !ok {
            sumMap[arr[idx]] = idx 
        } 
    }

    for idx, x := range arr {
        if x == 0 {
            ans = Max(ans, idx + 1)
        } else {
            val, ok := sumMap[x]
            if !ok || val == idx {
                continue
            }

            ans = Max(ans, idx - val)
        }
    }

    return ans
}
