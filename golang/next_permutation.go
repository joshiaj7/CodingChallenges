package golang

import (
	"sort"
)

/*
Space	: O(1)
Time	: O(n)
*/

func nextPermutation(nums []int)  {
    found := false
    n := len(nums)
    point := 0
	
	// check if there's nums[i] < nums[i+1]
	// store in index in point var
    for i := n-2; i >= 0; i-- {
        if nums[i] < nums[i+1] {
            found = true
            point = i
            break
        }
    } 
	
	// if not found, then the answer is sorted nums
    if !found {
        sort.Ints(nums)
    } else {
		// if found, swap nums[point] with element greater than nums[point] from behind
        for j := n-1; j >= 0; j-- {
            if nums[j] > nums[point] {
                nums[point], nums[j] = nums[j], nums[point]
                break
            }
		}
		
		// after swapped, reverse swapped sliced from pointed index
        for k, l := point+1, n-1; k < l; k, l = k + 1, l - 1 {
            nums[k], nums[l] = nums[l], nums[k]
        }
    }
}