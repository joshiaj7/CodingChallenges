package main

import (
	"golang/model"
	"strconv"
)

// Space : O(1)
// Time  : O(n)

func tree2str(root *model.TreeNode) string {
    s := ""
    
    if root != nil {
        s = strconv.Itoa(root.Val)
    
        if root.Left != nil {
            s += "(" + tree2str(root.Left) + ")"
        }

        if root.Left == nil && root.Right != nil {
            s += "()"
        }
        if root.Right != nil {
            s += "(" + tree2str(root.Right) + ")"
        }
    }
    
    return s
}