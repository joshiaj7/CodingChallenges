package main

// Space : O(n)
// Time  : O(n)

func twoSum(numbers []int, target int) []int {
    n := len(numbers)
    hashmap := make(map[int]int)
    
    for i := 0; i < n; i++ {
        hashmap[numbers[i]] = i+1
    }
    
    for i := 0; i < n; i++ {
        if _, ok := hashmap[target - numbers[i]]; ok {
            return []int{i+1, hashmap[target - numbers[i]]} 
        }
    }
    
    return []int{}
}