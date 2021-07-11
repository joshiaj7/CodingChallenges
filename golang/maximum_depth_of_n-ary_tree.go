package main

import "golang/model"

// Space : O(n)
// Time  : O(n)

func maxNaryNodeDepth(root *model.NaryNode) int {
    if root == nil {
        return 0
    }
    
    ans := 0
    stack := make([]*model.NaryNode, 0)
    stack = append(stack, root)
    
    for len(stack) > 0 {
        ans++
        temp := make([]*model.NaryNode, 0)
        
        for i := 0; i < len(stack); i++ {
            temp = append(temp, stack[i].Children...)
        }
        
        stack = temp
    }
    
    return ans
}