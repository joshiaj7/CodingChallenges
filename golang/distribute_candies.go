import "fmt"

// leetcode

func distributeCandies(candies int, num_people int) []int {
    ans := make([]int, num_people) 
    counter := 1
    idx := 0
    
    for candies > 0 {
        if candies - counter < 0 {
            ans[idx] += candies
            break
        } else {
            ans[idx] += counter
        }
        candies -= counter
        counter++
        if idx == len(ans)-1 {
            idx = 0
        } else {
            idx++
        }
    }
    
    return ans
}