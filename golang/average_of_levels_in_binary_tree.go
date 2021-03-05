package golang

// Space	: O(n)
// Time	: O(n)

import (
	"golang/model"
)


func averageOfLevels(root *model.TreeNode) []float64 {
    var ans []float64
    stack :=  []*model.TreeNode{root}
    
    for len(stack) > 0 {
        val := 0
        temp := []*model.TreeNode{}
        
        for i := 0; i < len(stack); i++ {
            val += stack[i].Val
            if stack[i].Left != nil {
                temp = append(temp, stack[i].Left)
            }
            if stack[i].Right != nil {
                temp = append(temp, stack[i].Right)
            }
        }

        ans = append(ans, float64(val) / float64(len(stack)))
        
        stack = temp
    }
    
    return ans
}
