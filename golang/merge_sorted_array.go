package main

/*
Space	: O(m)
Time	: O(m + n)
*/

func merge(nums1 []int, m int, nums2 []int, n int)  {
    p1, p2 := 0, 0

    var buf []int
    for i := 0; i < m; i++ {
        buf = append(buf, nums1[i])
    }
    
    for p1 < m && p2 < n {
        if buf[p1] < nums2[p2] {
            nums1[p1 + p2] = buf[p1]
            p1++
        } else {
            nums1[p1 + p2] = nums2[p2]
            p2++
        }
    } 
    
    for p1 < m {
        nums1[p1 + p2] = buf[p1]
        p1++
    }
    
    for p2 < n {
        nums1[p1 + p2] = nums2[p2]
        p2++
    }
}
