package main

/*
Space	: O(1)
Time	: O(log N)
*/

import "math"

func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
    t := (minutesToTest / minutesToDie) + 1
    
    x := 0
    for int(math.Pow(float64(t), float64(x))) < buckets {
        x++
    }
    
    return x
}
