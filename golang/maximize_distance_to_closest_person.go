package golang

// Space : O(1)
// Time	: O(n)


func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}


func maxDistToClosest(seats []int) int {
    var forward, backward, dist, mid, ans int
    
    n := len(seats)
    
    for k, v := range(seats) {
        // forward
        if v == 0 {
            forward++
            dist = max(dist, forward)
        } else {
            forward = 0
        }
        
        // backward
        if seats[n-1-k] == 0 {
            backward++
        } else {
            backward = 0
        }
        
    }
    
    if dist % 2 == 0 {
        mid = dist / 2
    } else {
        mid = (dist + 1) / 2
    }

    ans = max(ans, mid)
    ans = max(ans, forward)
    ans = max(ans, backward)
    return ans
}