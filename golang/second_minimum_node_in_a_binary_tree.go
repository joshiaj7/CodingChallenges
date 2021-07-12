package main

import "golang/model"

// Space : O(n)
// Time  : O(n)

func findSecondMinimumValue(root *model.TreeNode) int {
    s := []*model.TreeNode{root}
    ans := -1
    minv := root.Val
    
    for len(s) > 0 {
        node := s[0]
        s = s[1:]
        
        if (ans == -1 || node.Val < ans) && node.Val != minv {
            if node.Val < minv {
                minv, ans = node.Val, minv
            } else {
                ans = node.Val
            }
        } 
        
        if node.Left != nil {
            s = append(s, node.Left)
        }
        if node.Right != nil {
            s = append(s, node.Right)
        }
    }
    
    return ans
}