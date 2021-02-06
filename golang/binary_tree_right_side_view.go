package golang

import (
	"golang/model"
)


func rightSideView(root *model.TreeNode) []int {
    var ans []int
    stack := []*model.TreeNode{root}
    
    if root == nil {
        return ans
    }
    
    for len(stack) > 0 {
        var temp []*model.TreeNode
        for i := range stack {
            if i == (len(stack)-1) {
                ans = append(ans, stack[i].Val)
            }
            if stack[i].Left != nil {
                temp = append(temp, stack[i].Left)
            }
            if stack[i].Right != nil {
                temp = append(temp, stack[i].Right)
            }
        }
        
        stack = temp
    }

    return ans
}