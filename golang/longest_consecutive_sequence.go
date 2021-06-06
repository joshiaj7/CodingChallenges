package main

// Space : O(n)
// Time  : O(n)

func longestConsecutive(nums []int) int {
    ans := 0
    hashmap := make(map[int]int)
    
    for _, num := range nums {
        hashmap[num] = 1
    }
    
    for key, _ := range hashmap {
        best, j := 1, 1
        for {
            if _, ok := hashmap[key - j]; !ok {
                break
            }
            delete(hashmap, key - j)
            best, j = best + 1, j + 1
        }
        j = 1
        for {
            if _, ok := hashmap[key + j]; !ok {
                break
            }
            delete(hashmap, key + j)
            best, j = best + 1, j + 1
        }
        ans = Max(ans, best)
    }
    
    
    return ans
}