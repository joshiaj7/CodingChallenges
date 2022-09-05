package main

import "golang/model"

/*
Space	: O(n)
Time	: O(n)
*/

 func levelOrderNary(root *model.Node) [][]int {
    if root == nil {
        return [][]int{}
    }
    
    var ans [][]int
    stack := []*model.Node{root}

    for len(stack) > 0 {
        var temp []*model.Node
        var line []int
        
        for _, node := range stack {
            line = append(line, node.Val)
            
            if node.Children != nil {
                temp = append(temp, node.Children...)
            }
        }
        
        ans = append(ans, line)
        stack = temp
    }
    
    return ans
}
